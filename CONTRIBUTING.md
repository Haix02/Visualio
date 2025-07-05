# Contributing to Visualio 🤝

We love your input! We want to make contributing to Visualio as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

### Branch Naming Convention

- `feature/description` - for new features
- `bugfix/description` - for bug fixes
- `hotfix/description` - for critical fixes
- `docs/description` - for documentation updates
- `refactor/description` - for code refactoring

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Local Development
```bash
# 1. Fork and clone your fork
git clone https://github.com/YOUR_USERNAME/Visualio.git
cd Visualio

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install development dependencies
pip install pytest black flake8 mypy

# 5. Run the application
streamlit run app.py
```

### Code Style

We use several tools to maintain code quality:

#### Black (Code Formatting)
```bash
# Format all Python files
black .

# Check formatting without making changes
black --check .
```

#### Flake8 (Linting)
```bash
# Run linting
flake8 .

# With specific configuration
flake8 --max-line-length=88 --extend-ignore=E203,W503 .
```

#### MyPy (Type Checking)
```bash
# Run type checking
mypy . --ignore-missing-imports
```

### Testing

#### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_data_processor.py
```

#### Writing Tests
- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test names
- Include both positive and negative test cases
- Test edge cases and error conditions

Example test structure:
```python
def test_function_name():
    # Arrange
    input_data = ...
    expected_output = ...
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output
```

## Code Guidelines

### Python Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

### Documentation
- Update README.md if you change functionality
- Add docstrings to new functions
- Update type hints
- Include examples in docstrings when helpful

### Commit Messages
Follow conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(parser): add support for date range queries
fix(charts): resolve pie chart color issue
docs(readme): update installation instructions
```

## Issue Reporting

### Bug Reports
When filing a bug report, please include:

1. **Description**: Clear description of the issue
2. **Reproduction Steps**: Step-by-step instructions to reproduce
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: 
   - OS and version
   - Python version
   - Package versions
   - Browser (if applicable)
6. **Screenshots**: If applicable
7. **Sample Data**: If the issue involves specific data

### Feature Requests
When suggesting a feature:

1. **Use Case**: Explain why this feature would be useful
2. **Description**: Detailed description of the proposed feature
3. **Alternatives**: Any alternative solutions considered
4. **Implementation**: Ideas for how it could be implemented (optional)

## Project Structure

```
Visualio/
├── app.py                 # Main Streamlit application
├── data_processor.py      # Data loading and processing
├── nlp_parser.py         # Natural language processing
├── chart_generator.py    # Chart generation logic
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
├── README.md            # Project documentation
├── CHANGELOG.md         # Version history
├── DEPLOYMENT.md        # Deployment guide
├── examples/            # Example data and documentation
│   ├── data/           # Sample datasets
│   └── README.md       # Examples documentation
├── .streamlit/         # Streamlit configuration
├── .github/            # GitHub workflows
├── tests/              # Test files (if created)
└── docs/               # Additional documentation
```

## Code Review Process

1. **Automated Checks**: All PRs must pass CI checks
2. **Review Requirements**: At least one maintainer review
3. **Discussion**: Use PR comments for discussion
4. **Approval**: Maintainer approval required for merge

### Review Checklist

- [ ] Code follows style guidelines
- [ ] Tests are included and pass
- [ ] Documentation is updated
- [ ] No breaking changes (or properly documented)
- [ ] Commit messages are clear
- [ ] Code is well-commented
- [ ] Performance impact considered

## Release Process

1. Update version in `setup.py` and `app.py`
2. Update `CHANGELOG.md`
3. Create release branch
4. Run full test suite
5. Create GitHub release
6. Deploy to package index (if applicable)

## Getting Help

- 📝 [GitHub Issues](https://github.com/Haix02/Visualio/issues)
- 💬 [GitHub Discussions](https://github.com/Haix02/Visualio/discussions)
- 📧 Contact maintainers directly

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- CHANGELOG.md
- README.md acknowledgments
- Release notes

Thank you for contributing to Visualio! 🎉