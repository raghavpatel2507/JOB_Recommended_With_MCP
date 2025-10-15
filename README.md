# 🤖 AI Job Recommender with MCP

An intelligent job recommendation system that analyzes your resume using AI and provides personalized job recommendations from LinkedIn and Naukri. The system also includes an MCP (Model Context Protocol) server for integration with AI assistants.

## ✨ Features

- **📄 Resume Analysis**: Upload your PDF resume and get AI-powered analysis
- **🔍 Skill Gap Analysis**: Identify missing skills and areas for improvement
- **🚀 Career Roadmap**: Get personalized career development suggestions
- **💼 Job Recommendations**: Find relevant jobs from LinkedIn and Naukri
- **🤖 MCP Integration**: Built-in MCP server for AI assistant integration
- **🌐 Web Interface**: Beautiful Streamlit-based user interface

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: LangChain with Groq (GPT-OSS-120B model)
- **PDF Processing**: PyMuPDF
- **Job Scraping**: Apify Client (LinkedIn & Naukri scrapers)
- **MCP Server**: FastMCP
- **Environment**: Python 3.13+

## 📋 Prerequisites

Before running this project, make sure you have:

1. **Python 3.13+** installed
2. **API Keys** for the following services:
   - [Groq API Key](https://console.groq.com/) - for AI analysis
   - [Apify API Key](https://console.apify.com/) - for job scraping

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd JOB_Recommended_With_MCP
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv (recommended):
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   APIFY_API_KEY=your_apify_api_key_here
   ```

## 🎯 Usage

### Web Application

1. **Start the Streamlit app**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload your resume** (PDF format)

4. **Get AI analysis** including:
   - Resume summary
   - Skill gaps identification
   - Career roadmap suggestions

5. **Find job recommendations** from LinkedIn and Naukri

### MCP Server

The project includes an MCP server for integration with AI assistants:

1. **Start the MCP server**
   ```bash
   python mcp_server.py
   ```

2. **Available MCP tools**:
   - `fetchlinkedin`: Search for jobs on LinkedIn
   - `fetchnaukri`: Search for jobs on Naukri

## 📁 Project Structure

```
JOB_Recommended_With_MCP/
├── main.py                 # Streamlit web application
├── mcp_server.py          # MCP server implementation
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── __init__.py
    ├── helper.py         # PDF processing and AI utilities
    └── job_api.py        # Job scraping APIs
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | API key for Groq AI service | Yes |
| `APIFY_API_KEY` | API key for Apify scraping service | Yes |

### Job Search Parameters

You can customize job search parameters in `src/job_api.py`:

- **LinkedIn**: Location, number of jobs, proxy settings
- **Naukri**: Keywords, max jobs, freshness, sorting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [Groq](https://groq.com/) for AI processing
- [Apify](https://apify.com/) for job scraping services
- [LangChain](https://langchain.com/) for AI integration
- [FastMCP](https://github.com/jlowin/fastmcp) for MCP server implementation

## 🔮 Future Enhancements

- [ ] Support for multiple resume formats (DOCX, TXT)
- [ ] Integration with more job boards
- [ ] Advanced filtering and sorting options
- [ ] Resume optimization suggestions
- [ ] Job application tracking
- [ ] Email notifications for new matching jobs
- [ ] Company insights and reviews integration

---

**Made with ❤️ for job seekers everywhere!**
