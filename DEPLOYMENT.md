# Deployment Guide 🚀

This guide covers various ways to deploy Visualio for different use cases.

## Table of Contents
- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Cloud Deployment](#cloud-deployment)
- [Production Considerations](#production-considerations)

## Local Development

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Haix02/Visualio.git
cd Visualio

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Using Virtual Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Development Mode
For development with auto-reload:
```bash
streamlit run app.py --server.runOnSave true
```

## Docker Deployment

### Using Docker
```bash
# Build the image
docker build -t visualio .

# Run the container
docker run -p 8501:8501 visualio
```

### Using Docker Compose
```bash
# For development
docker-compose up

# For production
docker-compose --profile production up -d
```

### Docker Environment Variables
Set these environment variables for production:
```bash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## Cloud Deployment

### Streamlit Cloud
1. Fork the repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy using your GitHub repository
4. Set the main file path to `app.py`

### Heroku
1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### AWS EC2
1. Launch an EC2 instance (Ubuntu 20.04 recommended)
2. Install Docker:
```bash
sudo apt update
sudo apt install docker.io docker-compose
sudo usermod -aG docker $USER
```

3. Deploy:
```bash
git clone https://github.com/Haix02/Visualio.git
cd Visualio
docker-compose --profile production up -d
```

### Google Cloud Platform
1. Create a new project in GCP
2. Enable Cloud Run API
3. Build and deploy:
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/visualio
gcloud run deploy --image gcr.io/PROJECT_ID/visualio --platform managed
```

### DigitalOcean App Platform
1. Create a new app in DigitalOcean
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set run command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

## Production Considerations

### Security
- Use environment variables for sensitive configurations
- Implement authentication if needed
- Use HTTPS in production
- Regularly update dependencies

### Performance
- Set appropriate memory limits
- Use caching for data processing
- Monitor application performance
- Scale horizontally if needed

### Monitoring
- Implement health checks
- Set up logging
- Monitor resource usage
- Use error tracking (e.g., Sentry)

### Configuration
Create production-specific configurations:

`.streamlit/config.toml`:
```toml
[server]
headless = true
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[global]
developmentMode = false
```

### Backup and Recovery
- Regular data backups
- Database replication if using persistent storage
- Disaster recovery plan
- Version control for configurations

### Load Balancing
For high-traffic deployments:
- Use nginx as reverse proxy
- Implement session affinity
- Configure multiple app instances
- Use container orchestration (Kubernetes)

### Example Nginx Configuration
```nginx
upstream visualio {
    server app1:8501;
    server app2:8501;
}

server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://visualio;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Troubleshooting

### Common Issues
1. **Port already in use**: Change port in command or config
2. **Memory issues**: Increase container memory limits
3. **Dependencies conflicts**: Use virtual environments
4. **Permission errors**: Check file permissions and user rights

### Logs
View application logs:
```bash
# Docker
docker logs container_name

# Local
Check terminal output where streamlit is running
```

### Support
- Check GitHub Issues
- Review Streamlit documentation
- Contact development team

---

For more information, refer to the main [README.md](README.md) file.