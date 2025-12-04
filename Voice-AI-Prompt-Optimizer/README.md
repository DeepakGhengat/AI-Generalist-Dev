# AI Prompt Optimizer

Two powerful tools for working with AI prompts:

1. 🎤 **Voice to Prompt** - Speak and get markdown prompts
2. 🔄 **Prompt Optimizer** - Automatically optimize prompts with Claude/ChatGPT

---

## 🎤 Voice to Prompt

**Speak your ideas, get perfect markdown prompts!**

### Quick Start

```bash
# 1. Setup
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your-key

# 2. Install
pip install pyaudio openai anthropic python-dotenv

# 3. Run
python ultra_simple.py
```

**That's it!** Speak for 30 seconds, get a formatted markdown prompt.

### Example

**You speak:**
> "Create a prompt for a code review assistant that checks security, performance, and code quality"

**You get:**
```markdown
# Code Review Assistant

## Objective
Comprehensive code review focusing on security, performance, and quality.

## Review Areas

### Security
- Input validation
- SQL injection prevention
- Authentication checks
- Data encryption

### Performance
- Algorithm efficiency
- Database optimization
- Caching strategy

### Code Quality
- Style guidelines
- Documentation
- Error handling
- Test coverage
```

---

## 🔄 Prompt Optimizer

**Automatically improve prompts using AI and deep research.**

### Quick Start

```bash
# 1. Setup .env
cp .env.example .env

# Add your keys:
# ANTHROPIC_API_KEY=... (for Claude) OR
# OPENAI_API_KEY=...    (for ChatGPT)
# PERPLEXITY_API_KEY=...  (optional, for research)

# Set your model:
# PRIMARY_MODEL=CLAUDE  (or OPENAI)

# 2. Install
pip install anthropic openai python-dotenv requests matplotlib

# 3. Run
python optimize.py
```

### What It Does

1. **Tests** your prompt with various queries
2. **Analyzes** what works and what doesn't
3. **Researches** best practices with Perplexity AI
4. **Generates** improved versions
5. **Iterates** until target accuracy reached

### Features

- ✅ **Claude 4.5 Sonnet** or **ChatGPT** as primary model
- ✅ **Perplexity deep research** for optimization insights
- ✅ **Automatic testing** with query variations
- ✅ **Smart stopping** when target reached
- ✅ **Performance graphs** and detailed metrics
- ✅ **All config in .env** - easy to share

---

## 📋 Configuration

### .env File

```bash
# API Keys (at least one required)
ANTHROPIC_API_KEY=sk-ant-...     # For Claude
OPENAI_API_KEY=sk-...            # For ChatGPT/Whisper
PERPLEXITY_API_KEY=pplx-...      # Optional for research

# Choose your model
PRIMARY_MODEL=CLAUDE              # or OPENAI

# Model versions
CLAUDE_MODEL=claude-sonnet-4-20250514
OPENAI_MODEL=gpt-4
PERPLEXITY_MODEL=sonar

# Optimization settings
MAX_ITERATIONS=5
TARGET_ACCURACY=0.90
USE_PERPLEXITY=true
```

---

## 📁 Project Structure

```
AI-Prompt-Optimizer/
├── ultra_simple.py      # 🎤 Voice to prompt (47 lines)
├── optimize.py          # 🔄 Full optimizer (743 lines)
├── .env.example         # Configuration template
├── requirements.txt     # Dependencies
├── README.md           # This file
└── output/             # Results saved here
```

Clean and simple!

---

## 🔧 Installation

### macOS

```bash
# Install PortAudio for voice recording
brew install portaudio

# Install Python packages
pip install -r requirements.txt
```

### Linux

```bash
# Install PortAudio
sudo apt-get install portaudio19-dev

# Install Python packages
pip install -r requirements.txt
```

### Windows

```bash
# Usually works directly
pip install -r requirements.txt

# If pyaudio fails:
pip install pipwin
pipwin install pyaudio
```

---

## 💡 Usage Tips

### Voice to Prompt

1. **Speak clearly** - articulate your words
2. **Reduce background noise** - find a quiet space
3. **Be specific** - mention structure you want
4. **Natural speech** - "um" and "uh" are cleaned up automatically

### Prompt Optimizer

1. **Edit test queries** in `optimize.py` (line ~94) to match your use case
2. **Edit functions** (line ~107) to match your assistant's capabilities
3. **Adjust settings** in `.env` for different optimization strategies
4. **Review results** in `output/optimize_run_TIMESTAMP/`

---

## 🎯 Use Cases

### Voice to Prompt
- Quick prompt drafting
- Brainstorming sessions
- Meeting notes → prompts
- Hands-free creation
- Accessibility

### Prompt Optimizer
- Voice assistant optimization
- Chatbot prompt improvement
- Function calling accuracy
- A/B testing prompts
- Production deployment testing

---

## 🔍 Examples

### Voice to Prompt

```bash
# Record and speak
python ultra_simple.py

# Output saved to: prompt_20250103_143022.md
```

### Prompt Optimizer

```bash
# Run optimization
python optimize.py

# Output:
# 🚀 Voice Assistant Prompt Optimizer
# ============================================================
# Configuration:
#   - Primary Model: Claude claude-sonnet-4-20250514
#   - Max Iterations: 5
#   - Target Accuracy: 90%
#   - Perplexity Research: Enabled
# ============================================================
#
# 📊 ITERATION 1/5
# 📈 RESULTS:
#    Overall Score: 85.0%
#    Function Accuracy: 80.0%
#    🎯 New best score!
#
# 🔍 Researching optimization strategies with Perplexity...
# ✅ Research insights obtained
#
# 🔧 Generating improved prompt...
# [continues optimizing...]
```

---

## 🚀 Quick Command Reference

```bash
# Voice to Prompt
python ultra_simple.py

# Prompt Optimizer
python optimize.py

# Setup
cp .env.example .env
pip install -r requirements.txt

# View results
ls output/
```

---

## 📊 Performance

### Voice to Prompt
- **Speed**: ~30 seconds recording + 5-10 seconds processing
- **Quality**: Professional markdown with proper structure
- **Cost**: ~$0.01-0.05 per prompt

### Prompt Optimizer
- **Speed**: ~5-15 minutes (depends on iterations)
- **Improvement**: Typically 15-30% accuracy gain
- **Cost**: ~$1-3 per optimization run

---

Feel free to fork and customize!

---

## 🆘 Support

**Issues?**
1. Check .env has valid API keys
2. Run `pip install -r requirements.txt`
3. For voice: verify microphone works
4. Check internet connection

**Still stuck?** Open an issue on GitHub.

