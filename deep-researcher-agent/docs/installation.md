# Installation Guide

## Quick Start

1. **Download the package**
2. **Install dependencies:**
   ```bash
   pip install numpy
   ```
3. **Run the demo:**
   ```bash
   python examples/interactive_demo.py
   ```

## Detailed Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Extract the package** to your desired location
2. **Open terminal/command prompt** in the package directory
3. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Test the installation:**
   ```bash
   python examples/basic_usage.py
   ```

## Troubleshooting

### Common Issues

**Import Error:**
- Make sure you're in the correct directory
- Check that numpy is installed: `pip list | grep numpy`

**Python Version Error:**
- Update to Python 3.7+: Check with `python --version`

**Permission Error:**
- Use virtual environment or: `pip install --user numpy`

## Next Steps

After installation:
1. Try `examples/interactive_demo.py`
2. Try `examples/basic_usage.py`  
3. Read the main README.md for more information
4. Add your own documents and start researching!
