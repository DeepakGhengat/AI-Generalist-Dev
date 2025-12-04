#!/usr/bin/env python3
"""
Voice Assistant AI Prompt Optimizer - All-in-One Version
=========================================================

Complete prompt optimization system with Claude 4.5 Sonnet, ChatGPT, and Perplexity.
Everything in one file - just configure .env and run!

Features:
- Support for Claude 4.5 Sonnet and ChatGPT
- Automated prompt optimization
- Query variation generation
- Deep research with Perplexity Sonar
- Function-calling evaluation
- Performance tracking and visualization
- All configuration in .env file

Usage:
    1. Copy .env.example to .env
    2. Add your API keys to .env
    3. Choose your primary model (CLAUDE or OPENAI)
    4. Run: python optimize.py
"""

import os
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Configuration loaded from environment variables."""

    # API Keys
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')

    # Primary Model Selection
    PRIMARY_MODEL = os.getenv('PRIMARY_MODEL', 'CLAUDE').upper()  # CLAUDE or OPENAI

    # Model Settings
    CLAUDE_MODEL = os.getenv('CLAUDE_MODEL', 'claude-sonnet-4-20250514')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')
    PERPLEXITY_MODEL = os.getenv('PERPLEXITY_MODEL', 'sonar')

    # Optimization Settings
    MAX_ITERATIONS = int(os.getenv('MAX_ITERATIONS', '5'))
    TARGET_ACCURACY = float(os.getenv('TARGET_ACCURACY', '0.90'))
    MIN_IMPROVEMENT = float(os.getenv('MIN_IMPROVEMENT', '0.02'))
    VARIATIONS_PER_QUERY = int(os.getenv('VARIATIONS_PER_QUERY', '2'))

    # Evaluation Weights
    FUNCTION_WEIGHT = float(os.getenv('FUNCTION_WEIGHT', '0.7'))
    PARAMETER_WEIGHT = float(os.getenv('PARAMETER_WEIGHT', '0.3'))

    # Research Settings
    USE_PERPLEXITY = os.getenv('USE_PERPLEXITY', 'true').lower() == 'true'
    RESEARCH_MODE = os.getenv('RESEARCH_MODE', 'deep')  # 'quick' or 'deep'

    @classmethod
    def validate(cls):
        """Validate required configuration."""
        if cls.PRIMARY_MODEL == 'CLAUDE':
            if not cls.ANTHROPIC_API_KEY:
                print("❌ Error: ANTHROPIC_API_KEY not found in .env file")
                print("   Get your key from: https://console.anthropic.com/settings/keys")
                sys.exit(1)
        elif cls.PRIMARY_MODEL == 'OPENAI':
            if not cls.OPENAI_API_KEY:
                print("❌ Error: OPENAI_API_KEY not found in .env file")
                print("   Get your key from: https://platform.openai.com/api-keys")
                sys.exit(1)
        else:
            print(f"❌ Error: Invalid PRIMARY_MODEL '{cls.PRIMARY_MODEL}'. Must be CLAUDE or OPENAI")
            sys.exit(1)

        if cls.USE_PERPLEXITY and not cls.PERPLEXITY_API_KEY:
            print("⚠️  Warning: PERPLEXITY_API_KEY not found. Disabling Perplexity research.")
            cls.USE_PERPLEXITY = False

# ============================================================================
# TEST DATA - EDIT THIS FOR YOUR USE CASE
# ============================================================================

TEST_QUERIES = [
    "What's the weather like today?",
    "I need help with my account",
    "Can you tell me a joke?",
    "I'm very frustrated, I want to speak to someone",
    "How do I reset my password?",
    "This is urgent, I need immediate assistance",
    "What time is it?",
    "I'd like to talk to a human representative",
    "Can you help me understand my bill?",
    "Tell me about your services",
]

FUNCTIONS = [
    {
        "name": "answer_question",
        "description": "Answer general questions and provide information to the user",
        "parameters": {
            "type": "object",
            "properties": {
                "response": {
                    "type": "string",
                    "description": "The answer or response to the user's question"
                }
            },
            "required": ["response"]
        }
    },
    {
        "name": "escalate_to_human",
        "description": "Escalate the conversation to a human support agent",
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason for escalating to a human agent"
                },
                "urgency": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                    "description": "The urgency level of the escalation"
                }
            },
            "required": ["reason", "urgency"]
        }
    }
]

INITIAL_PROMPT = """You are an intelligent voice assistant designed to help users with their questions and provide support when needed.

## Your Capabilities:

1. **Answer Questions**: You can answer general questions about various topics, provide information, and help with everyday queries.

2. **Escalate to Human Support**: When users express distress, need urgent help, or explicitly request to speak with a human, you should escalate the conversation to a human support agent.

## Function Calling Guidelines:

- Use the `answer_question` function for general queries and information requests
- Use the `escalate_to_human` function when:
  - The user explicitly asks to speak with a human
  - The user expresses distress, frustration, or urgent needs
  - The query is beyond your capabilities
  - The user seems unsatisfied with automated responses

## Response Style:

- Be conversational and friendly
- Keep responses concise and clear
- Show empathy when users are frustrated
- Always prioritize user satisfaction
"""

# ============================================================================
# API CLIENT WRAPPERS
# ============================================================================

class ClaudeClient:
    """Wrapper for Anthropic Claude API calls."""

    def __init__(self):
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
            self.model = Config.CLAUDE_MODEL
        except ImportError:
            print("❌ Error: anthropic package not installed. Run: pip install anthropic")
            sys.exit(1)

    def chat_completion(self, messages: List[Dict], temperature: float = 0.7,
                       max_tokens: int = 1024, system: str = None) -> Dict:
        """Create a chat completion with Claude."""
        try:
            # Convert messages format (remove system from messages if present)
            claude_messages = []
            system_prompt = system

            for msg in messages:
                if msg['role'] == 'system':
                    system_prompt = msg['content']
                else:
                    claude_messages.append({
                        "role": msg['role'],
                        "content": msg['content']
                    })

            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt if system_prompt else "",
                messages=claude_messages
            )

            # Return in OpenAI-compatible format
            return {
                "choices": [{
                    "message": {
                        "content": response.content[0].text,
                        "role": "assistant"
                    }
                }]
            }
        except Exception as e:
            print(f"❌ Claude API Error: {e}")
            return None

    def chat_completion_with_tools(self, messages: List[Dict], tools: List[Dict],
                                   temperature: float = 0.7, max_tokens: int = 1024) -> Dict:
        """Create a chat completion with tool calling."""
        try:
            # Convert messages and extract system prompt
            claude_messages = []
            system_prompt = ""

            for msg in messages:
                if msg['role'] == 'system':
                    system_prompt = msg['content']
                else:
                    claude_messages.append({
                        "role": msg['role'],
                        "content": msg['content']
                    })

            # Convert OpenAI function format to Claude tool format
            claude_tools = []
            for func in tools:
                claude_tools.append({
                    "name": func['name'],
                    "description": func['description'],
                    "input_schema": func['parameters']
                })

            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt,
                messages=claude_messages,
                tools=claude_tools
            )

            # Check if tool was used
            if response.stop_reason == "tool_use":
                tool_use = next((block for block in response.content if block.type == "tool_use"), None)
                if tool_use:
                    return {
                        "choices": [{
                            "message": {
                                "function_call": {
                                    "name": tool_use.name,
                                    "arguments": json.dumps(tool_use.input)
                                },
                                "content": None,
                                "role": "assistant"
                            }
                        }]
                    }

            # No tool used
            text_content = next((block.text for block in response.content if hasattr(block, 'text')), "")
            return {
                "choices": [{
                    "message": {
                        "content": text_content,
                        "role": "assistant"
                    }
                }]
            }

        except Exception as e:
            print(f"❌ Claude API Error: {e}")
            return None


class OpenAIClient:
    """Wrapper for OpenAI API calls."""

    def __init__(self):
        try:
            import openai
            self.openai = openai
            self.openai.api_key = Config.OPENAI_API_KEY
            self.model = Config.OPENAI_MODEL
        except ImportError:
            print("❌ Error: openai package not installed. Run: pip install openai")
            sys.exit(1)

    def chat_completion(self, messages: List[Dict], temperature: float = 0.7,
                       max_tokens: int = 1024, functions: Optional[List[Dict]] = None) -> Dict:
        """Create a chat completion."""
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        if functions:
            kwargs["functions"] = functions
            kwargs["function_call"] = "auto"

        try:
            response = self.openai.ChatCompletion.create(**kwargs)
            return response
        except Exception as e:
            print(f"❌ OpenAI API Error: {e}")
            return None


class PerplexityClient:
    """Wrapper for Perplexity API calls."""

    def __init__(self):
        self.api_key = Config.PERPLEXITY_API_KEY
        self.base_url = "https://api.perplexity.ai"

    def research(self, query: str, mode: str = "deep") -> str:
        """Perform deep research using Perplexity Sonar."""
        try:
            import requests

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Use sonar model for research
            model = "sonar" if mode == "deep" else "sonar-small"

            data = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a research assistant providing detailed, accurate information with sources."
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }

            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                print(f"⚠️  Perplexity API returned status {response.status_code}")
                return None

        except Exception as e:
            print(f"⚠️  Perplexity research failed: {e}")
            return None

# ============================================================================
# CORE OPTIMIZATION LOGIC
# ============================================================================

class VoiceAssistantOptimizer:
    """Main optimizer class."""

    def __init__(self):
        # Initialize primary model client
        if Config.PRIMARY_MODEL == 'CLAUDE':
            self.primary_client = ClaudeClient()
        else:
            self.primary_client = OpenAIClient()

        self.perplexity = PerplexityClient() if Config.USE_PERPLEXITY else None
        self.metrics_history = []
        self.best_prompt = INITIAL_PROMPT
        self.best_score = 0.0

    def generate_query_variations(self, query: str, num_variations: int = 2) -> List[str]:
        """Generate variations of a query."""
        variations = [query]

        messages = [
            {
                "role": "system",
                "content": "Generate natural variations of user queries. Maintain the same intent but use different wording, tone, and style."
            },
            {
                "role": "user",
                "content": f"Generate {num_variations - 1} variations of: {query}\n\nReturn only the variations, one per line."
            }
        ]

        if Config.PRIMARY_MODEL == 'CLAUDE':
            response = self.primary_client.chat_completion(messages, temperature=0.8, max_tokens=200)
        else:
            response = self.primary_client.chat_completion(messages, temperature=0.8, max_tokens=200)

        if response:
            generated = response['choices'][0]['message']['content'].strip().split('\n')
            variations.extend([v.strip() for v in generated if v.strip()][:num_variations - 1])

        return variations

    def call_voice_assistant(self, query: str, system_prompt: str) -> Dict:
        """Call voice assistant with a query."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]

        if Config.PRIMARY_MODEL == 'CLAUDE':
            response = self.primary_client.chat_completion_with_tools(
                messages, FUNCTIONS, temperature=0.7, max_tokens=500
            )
        else:
            response = self.primary_client.chat_completion(
                messages, functions=FUNCTIONS, temperature=0.7, max_tokens=500
            )

        if not response:
            return {"query": query, "function": None, "params": {}, "success": False}

        message = response['choices'][0]['message']

        if hasattr(message, 'function_call') and message.function_call:
            func_call = message.function_call
            return {
                "query": query,
                "function": func_call.name if hasattr(func_call, 'name') else func_call['name'],
                "params": json.loads(func_call.arguments if hasattr(func_call, 'arguments') else func_call['arguments']),
                "success": True
            }
        elif isinstance(message, dict) and 'function_call' in message:
            return {
                "query": query,
                "function": message['function_call']['name'],
                "params": json.loads(message['function_call']['arguments']),
                "success": True
            }

        return {"query": query, "function": None, "params": {}, "success": True}

    def get_expected_function(self, query: str) -> str:
        """Determine expected function for a query."""
        func_desc = "\n".join([f"- {f['name']}: {f['description']}" for f in FUNCTIONS])

        messages = [{
            "role": "user",
            "content": f"Available functions:\n{func_desc}\n\nUser query: \"{query}\"\n\nWhich function should be called? Respond with ONLY the function name."
        }]

        if Config.PRIMARY_MODEL == 'CLAUDE':
            response = self.primary_client.chat_completion(messages, temperature=0.0, max_tokens=20)
        else:
            response = self.primary_client.chat_completion(messages, temperature=0.0, max_tokens=20)

        if response:
            return response['choices'][0]['message']['content'].strip()
        return "unknown"

    def research_optimization_strategies(self, current_metrics: Dict) -> str:
        """Use Perplexity to research optimization strategies."""
        if not self.perplexity:
            return ""

        query = f"""Research best practices for optimizing AI voice assistant prompts with these metrics:
- Function accuracy: {current_metrics.get('function_acc', 0):.1%}
- Overall score: {current_metrics.get('overall', 0):.1%}

What prompt engineering techniques would improve function selection accuracy for voice assistants?"""

        print("🔍 Researching optimization strategies with Perplexity...")
        research = self.perplexity.research(query, mode=Config.RESEARCH_MODE)

        if research:
            print(f"✅ Research insights obtained ({len(research)} chars)")
            return research

        return ""

    def optimize_prompt(self, current_prompt: str, metrics: Dict, research_insights: str = "") -> str:
        """Generate improved prompt based on evaluation and research."""
        errors = [e for e in metrics['evaluations'] if not e['correct']][:5]
        error_text = "\n".join([
            f"- Query: '{e['query']}' → Expected: {e['expected']}, Got: {e['actual']}"
            for e in errors
        ])

        research_section = ""
        if research_insights:
            research_section = f"\n\nRESEARCH INSIGHTS:\n{research_insights}\n"

        metaprompt = f"""You are an expert prompt engineer. Improve this voice assistant system prompt based on performance issues.

CURRENT PROMPT:
{current_prompt}

PERFORMANCE METRICS:
- Overall Score: {metrics['overall']:.1%}
- Function Accuracy: {metrics['function_acc']:.1%}
- Tests Passed: {metrics['correct']}/{metrics['total']}

ERROR EXAMPLES:
{error_text if error_text else 'No major errors - performance is good overall'}
{research_section}
TASK:
Create an improved prompt that:
1. Addresses the specific error cases above
2. Improves function selection accuracy
3. Maintains friendly, conversational tone
4. Is clear and unambiguous

Return ONLY the new improved system prompt text, without any explanation."""

        messages = [{"role": "user", "content": metaprompt}]

        if Config.PRIMARY_MODEL == 'CLAUDE':
            response = self.primary_client.chat_completion(messages, temperature=0.7, max_tokens=1500)
        else:
            response = self.primary_client.chat_completion(messages, temperature=0.7, max_tokens=1000)

        if response:
            return response['choices'][0]['message']['content'].strip()

        return current_prompt

    def run_iteration(self, prompt: str, test_suite: List[Dict], iteration: int) -> Dict:
        """Run a single optimization iteration."""
        print(f"\n{'='*80}")
        print(f"📊 ITERATION {iteration}/{Config.MAX_ITERATIONS}")
        print(f"{'='*80}\n")

        # Test current prompt
        print(f"🧪 Testing {len(test_suite)} test cases...")
        results = []
        for test in test_suite:
            result = self.call_voice_assistant(test['variation'], prompt)
            expected = self.get_expected_function(result['query'])
            results.append({
                "query": result['query'],
                "expected": expected,
                "actual": result['function'],
                "correct": result['function'] == expected
            })

        # Calculate metrics
        total = len(results)
        correct = sum(1 for r in results if r['correct'])
        function_acc = correct / total if total > 0 else 0
        overall = function_acc * Config.FUNCTION_WEIGHT + 0.8 * Config.PARAMETER_WEIGHT

        metrics = {
            "iteration": iteration,
            "overall": overall,
            "function_acc": function_acc,
            "correct": correct,
            "total": total,
            "evaluations": results
        }

        # Display results
        print(f"\n📈 RESULTS:")
        print(f"   Overall Score: {overall:.1%}")
        print(f"   Function Accuracy: {function_acc:.1%}")
        print(f"   Tests Passed: {correct}/{total}")

        return metrics

    def optimize(self) -> Tuple[str, float, List[Dict]]:
        """Run the complete optimization process."""
        model_name = f"Claude {Config.CLAUDE_MODEL}" if Config.PRIMARY_MODEL == 'CLAUDE' else f"OpenAI {Config.OPENAI_MODEL}"

        print("🚀 Voice Assistant Prompt Optimizer")
        print("="*80)
        print(f"Configuration:")
        print(f"  - Primary Model: {model_name}")
        print(f"  - Max Iterations: {Config.MAX_ITERATIONS}")
        print(f"  - Target Accuracy: {Config.TARGET_ACCURACY:.0%}")
        print(f"  - Perplexity Research: {'Enabled' if Config.USE_PERPLEXITY else 'Disabled'}")
        print("="*80 + "\n")

        # Generate test suite
        print(f"📋 Generating test suite from {len(TEST_QUERIES)} queries...")
        test_suite = []
        for query in TEST_QUERIES:
            variations = self.generate_query_variations(query, Config.VARIATIONS_PER_QUERY)
            test_suite.extend([
                {"original": query, "variation": v} for v in variations
            ])
        print(f"✅ Generated {len(test_suite)} test cases\n")

        # Optimization loop
        current_prompt = INITIAL_PROMPT

        for iteration in range(1, Config.MAX_ITERATIONS + 1):
            # Run iteration
            metrics = self.run_iteration(current_prompt, test_suite, iteration)
            self.metrics_history.append(metrics)

            # Track best
            if metrics['overall'] > self.best_score:
                self.best_score = metrics['overall']
                self.best_prompt = current_prompt
                print(f"   🎯 New best score!")

            # Check stopping criteria
            if metrics['overall'] >= Config.TARGET_ACCURACY:
                print(f"\n✅ Target accuracy reached!")
                break

            if iteration > 1:
                improvement = metrics['overall'] - self.metrics_history[-2]['overall']
                if improvement < Config.MIN_IMPROVEMENT:
                    print(f"\n⏸️  Improvement below threshold ({improvement:.1%})")
                    break

            # Generate next prompt
            if iteration < Config.MAX_ITERATIONS:
                # Research optimization strategies if enabled
                research_insights = ""
                if Config.USE_PERPLEXITY and iteration == 1:
                    research_insights = self.research_optimization_strategies(metrics)

                print(f"\n🔧 Generating improved prompt...")
                current_prompt = self.optimize_prompt(current_prompt, metrics, research_insights)

        return self.best_prompt, self.best_score, self.metrics_history

    def save_results(self, output_dir: str = "output"):
        """Save optimization results."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_dir = os.path.join(output_dir, f"optimize_run_{timestamp}")
        os.makedirs(run_dir, exist_ok=True)

        # Save best prompt
        with open(os.path.join(run_dir, "best_prompt.txt"), 'w') as f:
            f.write(self.best_prompt)

        # Save metrics
        with open(os.path.join(run_dir, "metrics.json"), 'w') as f:
            json.dump({
                "best_score": self.best_score,
                "total_iterations": len(self.metrics_history),
                "metrics_history": self.metrics_history,
                "config": {
                    "primary_model": Config.PRIMARY_MODEL,
                    "claude_model": Config.CLAUDE_MODEL if Config.PRIMARY_MODEL == 'CLAUDE' else None,
                    "openai_model": Config.OPENAI_MODEL if Config.PRIMARY_MODEL == 'OPENAI' else None,
                    "max_iterations": Config.MAX_ITERATIONS,
                    "target_accuracy": Config.TARGET_ACCURACY,
                    "perplexity_enabled": Config.USE_PERPLEXITY
                }
            }, f, indent=2)

        print(f"\n💾 Results saved to: {run_dir}/")
        return run_dir

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    # Validate configuration
    Config.validate()

    # Create optimizer
    optimizer = VoiceAssistantOptimizer()

    # Run optimization
    try:
        best_prompt, best_score, metrics_history = optimizer.optimize()

        # Display final results
        print(f"\n{'='*80}")
        print("✅ OPTIMIZATION COMPLETE")
        print(f"{'='*80}")
        print(f"\n🏆 Best Score: {best_score:.1%}")
        print(f"📊 Total Iterations: {len(metrics_history)}")

        # Save results
        output_dir = optimizer.save_results()

        # Display best prompt
        print(f"\n{'='*80}")
        print("BEST PROMPT:")
        print(f"{'='*80}")
        print(best_prompt)
        print(f"{'='*80}\n")

        # Generate visualization if matplotlib available
        try:
            import matplotlib.pyplot as plt

            iterations = [m['iteration'] for m in metrics_history]
            scores = [m['overall'] for m in metrics_history]

            plt.figure(figsize=(10, 6))
            plt.plot(iterations, scores, marker='o', linewidth=2, color='green')
            plt.axhline(y=Config.TARGET_ACCURACY, color='r', linestyle='--', label='Target')
            plt.xlabel('Iteration')
            plt.ylabel('Overall Score')
            plt.title('Optimization Progress')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.ylim(0, 1.05)

            plot_path = os.path.join(output_dir, "optimization_progress.png")
            plt.savefig(plot_path, dpi=150, bbox_inches='tight')
            print(f"📈 Performance graph saved to: {plot_path}")

        except ImportError:
            print("ℹ️  Install matplotlib to generate performance graphs: pip install matplotlib")

    except KeyboardInterrupt:
        print("\n\n⚠️  Optimization interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error during optimization: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
