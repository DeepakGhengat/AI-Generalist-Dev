# 🔍 Advanced AI Research System

A comprehensive research platform that combines multi-engine web scraping, AI-powered analysis, and dual-model evaluation to deliver high-quality research reports with full transparency and error handling.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-purple)
![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-red)

## 🌟 Key Features

### 🚀 Multi-Engine Web Scraping
- **DuckDuckGo & Brave Search**: Direct HTML scraping without API dependencies
- **Real-time Progress Tracking**: Live display of link discovery and scraping progress
- **Comprehensive JSON Saving**: Detailed metadata, performance metrics, and error tracking
- **Source Attribution**: Track which search engine provided each result
- **Performance Analytics**: Processing times, success rates, content statistics

### 🤖 AI-Powered Agentic Search
- **Strategic Search Planning**: AI agents plan multiple targeted searches
- **Progressive Refinement**: Iterative approach for comprehensive coverage
- **Comprehensive Reporting**: Structured markdown reports with executive summaries
- **Built-in Web Search**: Uses OpenAI Agents SDK with integrated search capabilities

### 🔥 Deep Search Capabilities (ENABLED!)
- **Deep ChatGPT Research**: Iterative refinement with progressive depth
- **Deep Claude-Style Research**: Systematic analysis with critical evaluation
- **Comparative Analysis**: Side-by-side comparison of different AI approaches
- **Multi-Phase Processing**: 5+ iterations with gap identification and targeted follow-up

### 📊 Dual-Model Evaluation System
- **GPT-4 + Claude Assessment**: Parallel evaluation for consensus scoring
- **Fallback Mechanisms**: Heuristic scoring when APIs are unavailable
- **Quality Gates**: Automatic approval/rejection based on consensus scores
- **Detailed Metrics**: Accuracy, completeness, relevance, clarity, and depth scoring

### 🎯 Beautiful Web Interface
- **Gradio-Powered UI**: Professional web interface with real-time updates
- **Multiple Search Types**: Standard agentic, combined, explorer-only, and deep search modes
- **File Analysis**: Automatic detection and analysis of research files
- **Configuration Controls**: Real-time adjustment of search parameters
- **API Status Monitoring**: Live checking of service availability

## 📋 Prerequisites

### Required Dependencies
```bash
pip install openai anthropic agents gradio pandas jupyter python-dotenv
```

### API Keys Required
- **OpenAI API Key**: For GPT-4 evaluation and agentic search
- **Anthropic API Key**: For Claude evaluation (optional, has fallback)

### Environment Setup
Create a `.env` file in your project directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## 🚀 Quick Start

### 1. Installation
```bash
git clone <your-repo>
cd advanced-research-system
pip install -r requirements.txt
```

### 2. Configuration
Edit the configuration variables in **Cell 2** of the notebook:
```python
# Web scraping configuration
MAX_LINKS_TO_EXTRACT = 20      # Links to extract from search results
MAX_URLS_TO_SCRAPE = 5         # URLs to scrape content from
MAX_SEARCH_RESULTS = 10        # Results per search engine

# Agentic search configuration  
MAX_STRATEGIC_SEARCHES = 3     # Number of strategic searches
SEARCH_CONTEXT_SIZE = "medium" # "small", "medium", "large"
REPORT_MIN_LENGTH = 1000       # Minimum report length

# Deep search configuration (NOW ENABLED!)
DEEP_SEARCH_ITERATIONS = 5     # Number of deep search iterations
DEEP_SEARCH_REFINEMENT = True  # Enable search refinement
```

### 3. Launch System
Run all cells in the Jupyter notebook. The Gradio interface will auto-launch at `http://localhost:7860`

## 🎛️ Usage Examples

### Standard Agentic Search with Evaluation
```python
# Complete research with AI evaluation
results = await run_research("impact of artificial intelligence on healthcare")

# Results include:
# - Comprehensive research report
# - GPT-4 and Claude evaluations  
# - Quality approval/rejection
# - Saved JSON file with full details
```

### Combined Explorer + Agentic Search
```python
# Web scraping + AI analysis
results = await run_combined_research("renewable energy trends 2024")

# Provides:
# - Raw scraped web data
# - AI-synthesized insights
# - Combined analysis report
```

### Explorer-Only Research (Enhanced)
```python
# Direct web scraping with detailed tracking
results = await run_explorer_only_research("climate change policies")

# Features:
# - Real-time link discovery
# - Detailed scraping progress
# - Performance metrics
# - Comprehensive JSON metadata
```

### 🔥 Deep Search (NEW!)
```python
# Deep ChatGPT iterative research
results = await run_deep_chatgpt_research("quantum computing applications")

# Deep Claude-style systematic research  
results = await run_deep_claude_research("blockchain scalability solutions")

# Comparative deep analysis
results = await run_comparative_deep_research("AI ethics frameworks")
```

### File Analysis
```python
# Analyze any research file
evaluation = await universal_json_evaluator("results.json", "original query")

# Explorer-specific analysis
analysis = display_explorer_json_analysis("explorer_search_20241201_143022.json")
```

## 📁 File Structure

```
workspace/
├── data/                           # All results saved here
│   ├── explorer_search_*.json      # Explorer search results
│   ├── combined_search_*.json      # Combined search results  
│   ├── evaluation_*.json           # Evaluation results
│   ├── deep_chatgpt_*.json         # Deep ChatGPT results
│   ├── deep_claude_style_*.json    # Deep Claude results
│   └── comparative_deep_*.json     # Comparative analysis
├── results/                        # Additional result files
└── Deepsearch_AI_and_Search_Engine.ipynb
```

## 🔧 Configuration Options

### Performance Presets

#### 🚀 High-Intensity Research
```python
MAX_LINKS_TO_EXTRACT = 50
MAX_URLS_TO_SCRAPE = 10  
MAX_STRATEGIC_SEARCHES = 7
DEEP_SEARCH_ITERATIONS = 10
SEARCH_CONTEXT_SIZE = "large"
REPORT_MIN_LENGTH = 2000
```

#### ⚡ Fast & Light Setup  
```python
MAX_LINKS_TO_EXTRACT = 10
MAX_URLS_TO_SCRAPE = 3
MAX_STRATEGIC_SEARCHES = 2
DEEP_SEARCH_ITERATIONS = 3
SEARCH_CONTEXT_SIZE = "small"
REPORT_MIN_LENGTH = 500
```

#### ⚖️ Balanced Configuration (Default)
```python
MAX_LINKS_TO_EXTRACT = 20
MAX_URLS_TO_SCRAPE = 5
MAX_STRATEGIC_SEARCHES = 3
DEEP_SEARCH_ITERATIONS = 5
SEARCH_CONTEXT_SIZE = "medium"
REPORT_MIN_LENGTH = 1000
```

## 🌐 Search Engines

### Currently Active
- **✅ DuckDuckGo**: Privacy-focused search with comprehensive results
- **✅ Brave Search**: Independent search engine with quality results

### Disabled (Cost Optimization)
- **🚫 Google Search**: Commented out to avoid API costs
  - Uncomment Google functions in Cell 4 to re-enable
  - Requires RapidAPI Google Search subscription

## 📊 File Types & Analysis

### 🔍 Explorer Results (`explorer_search_*.json`)
**Features:**
- Complete link discovery tracking
- Scraping performance metrics
- Success/failure analysis by engine
- Content length and processing time statistics
- Automatic query detection for analysis

**Analysis Provides:**
- Engine-by-engine performance breakdown
- Link success rates and failure reasons
- Content distribution and quality metrics
- Processing time analysis
- Sample content previews

### 📄 Research Reports (`evaluation_*.json`)  
**Features:**
- AI-generated research reports
- Dual-model evaluation scores
- Quality assessment and recommendations
- Follow-up questions and insights

**Analysis Provides:**
- GPT-4 and Claude evaluation scores
- Consensus quality assessment
- Strengths and improvement areas
- Actionable recommendations

### 🔄 Combined Search (`combined_search_*.json`)
**Features:**
- Explorer + agentic search results
- Integrated analysis of both approaches
- Comprehensive coverage metrics

**Analysis Provides:**
- Unified view of all search methods
- Cross-validation between sources
- Coverage gap identification

### 🔥 Deep Search Results (`deep_*_*.json`)
**Features:**
- Multi-iteration research progression
- Progressive refinement tracking
- Comparative analysis between AI approaches
- Enhanced depth and coverage

**Analysis Provides:**
- Iteration-by-iteration improvement tracking
- Methodology comparison and effectiveness
- Research depth and quality progression

## 🛠️ API Error Handling

### Robust Fallback System
The system includes comprehensive error handling with automatic fallbacks:

#### Claude API Issues (Error 529 - Overloaded)
- **Automatic Retries**: 3 attempts with exponential backoff
- **Fallback Evaluation**: Heuristic scoring when unavailable
- **Graceful Degradation**: GPT-4 evaluation continues normally
- **Status Monitoring**: Real-time API availability checking

#### GPT-4 API Issues
- **Rate Limit Handling**: Automatic retry with delays
- **Authentication Checking**: Clear error messages for API key issues
- **Billing Verification**: Guidance for account setup
- **Alternative Paths**: Claude evaluation continues independently

#### Fallback Evaluation Features
- **Heuristic Scoring**: Content-length based quality assessment
- **Conservative Estimates**: Reliable baseline quality scores
- **Clear Labeling**: Explicit indication when fallbacks are used
- **Re-evaluation Support**: Easy retry when APIs recover

### API Status Monitoring
```python
# Check current API availability
status = await test_api_availability()

# Returns:
# - GPT-4 availability status
# - Claude availability status  
# - Recommendations for optimization
# - Troubleshooting guidance
```

## 🎯 Advanced Features

### 🔥 Deep Search Capabilities
- **Multi-Iteration Analysis**: 5+ cycles of progressive refinement
- **Gap Identification**: Systematic identification of research gaps
- **Methodology Comparison**: ChatGPT vs Claude-style approaches
- **Enhanced Depth**: Superior analysis quality and comprehensiveness

### 📈 Enhanced Explorer Features
- **Real-Time Progress**: Live display of scraping progress
- **Link Attribution**: Track source of every discovered link
- **Performance Metrics**: Processing times and success rates
- **Error Analysis**: Detailed failure tracking and categorization
- **Content Analytics**: Text length distribution and quality metrics

### 🎨 Professional Web Interface
- **Auto-Launch**: Automatic Gradio interface startup
- **Configuration Controls**: Real-time parameter adjustment
- **File Management**: Easy access to recent research files
- **Status Monitoring**: Live API availability checking
- **Help System**: Comprehensive user guidance

### 🔄 Universal File Analyzer
```python
# Automatically detects and analyzes any research file type
analysis = await universal_json_evaluator(filepath, query)

# Supports:
# - Explorer search results
# - Agentic research reports
# - Combined search outputs  
# - Deep search results
# - Evaluation files
```

## 🚨 Troubleshooting

### Common Issues & Solutions

#### Slow Performance
- **Reduce** `MAX_URLS_TO_SCRAPE` and `MAX_LINKS_TO_EXTRACT`
- **Increase** `SCRAPING_TIMEOUT` for slow websites
- **Use** "small" `SEARCH_CONTEXT_SIZE` for faster processing

#### Empty or Poor Results
- **Try different search terms** - be more specific or broader
- **Increase** `MAX_SEARCH_RESULTS` for more comprehensive coverage
- **Check** search engine accessibility (some sites may block scrapers)

#### API Errors
- **OpenAI Issues**: Check API key, billing, and rate limits
- **Claude Issues**: Usually temporary overload - wait 2-5 minutes
- **Fallback Mode**: System continues with heuristic evaluation

#### File Analysis Errors
- **Check file path** accuracy and file existence
- **Provide original query** for non-explorer files
- **Verify file format** - must be valid JSON

#### Gradio Interface Issues
- **Port conflicts**: Change `PORT = 7860` to different number
- **Browser cache**: Clear cache or try incognito mode
- **Firewall**: Ensure port 7860 is allowed

### Emergency Procedures

#### Both APIs Down
1. System continues with fallback evaluations
2. Focus on research content quality
3. Manually verify key facts from provided sources
4. Re-evaluate when APIs recover

#### Complete System Reset
```python
# Restart kernel and rerun all cells
# Clear workspace if needed:
import shutil
shutil.rmtree("workspace", ignore_errors=True)
```

## 🎓 Best Practices

### Research Quality
1. **Use specific queries** for focused research
2. **Increase iterations** for complex topics
3. **Enable deep search** for controversial subjects
4. **Cross-validate** findings across multiple sources

### Performance Optimization
1. **Monitor API status** regularly
2. **Use off-peak hours** for better availability
3. **Space out requests** to avoid rate limiting
4. **Adjust configuration** based on research complexity

### File Management
1. **Regular cleanup** of old result files
2. **Meaningful queries** for easy file identification
3. **Backup important** research before system updates
4. **Use file analysis** to review past research

## 📚 Additional Resources

### Configuration Guide
- See **Cell 14** for comprehensive configuration options
- Use Gradio interface sliders for temporary adjustments
- Restart kernel after permanent configuration changes

### API Documentation
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Agents SDK Documentation](https://github.com/openai/agents)

### Gradio Interface
- **Main Search**: Primary research interface
- **File Analysis**: Analyze existing research files
- **System Config**: Monitor APIs and adjust settings
- **Help**: Comprehensive user guidance

## 🎉 System Capabilities Summary

### ✅ Fully Operational Features
- Multi-engine web scraping (DuckDuckGo + Brave)
- AI-powered agentic search with OpenAI Agents SDK
- **🔥 Deep search capabilities (ChatGPT + Claude-style)**
- Dual-model evaluation (GPT-4 + Claude)
- Comprehensive Gradio web interface
- Enhanced explorer features with detailed JSON
- Universal file analysis and type detection
- Robust error handling with automatic fallbacks
- Real-time progress monitoring and status updates

### 🎯 Ready for Production
This system is fully operational and ready for advanced research tasks, providing transparency, reliability, and comprehensive analysis capabilities.

---

**🚀 Start your advanced research journey today!**
