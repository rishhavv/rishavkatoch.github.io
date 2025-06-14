.PHONY: build clean new-post new-project serve

# Python interpreter
PYTHON := python3

# Directories
BLOG_DIR := blog/_posts
PROJECTS_DIR := projects/_posts
SITE_DIR := _site

# Build the site
build:
	@echo "Building site..."
	@$(PYTHON) build.py
	@echo "Site built successfully in $(SITE_DIR)/"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -rf $(SITE_DIR)
	@echo "Clean complete"

# Create a new blog post
new-post:
	@read -p "Enter post title (will be converted to slug): " title; \
	slug=$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-'); \
	date=$$(date +%Y-%m-%d); \
	cp $(BLOG_DIR)/template.md "$(BLOG_DIR)/$$date-$$slug.md"; \
	echo "Created new blog post: $(BLOG_DIR)/$$date-$$slug.md"

# Create a new project
new-project:
	@read -p "Enter project name (will be converted to slug): " name; \
	slug=$$(echo "$$name" | tr '[:upper:]' '[:lower:]' | tr ' ' '-'); \
	date=$$(date +%Y-%m-%d); \
	cp $(PROJECTS_DIR)/template.md "$(PROJECTS_DIR)/$$date-$$slug.md"; \
	echo "Created new project: $(PROJECTS_DIR)/$$date-$$slug.md"

# Serve the site locally (requires Python's http.server)
serve:
	@echo "Serving site at http://localhost:8000"
	@cd $(SITE_DIR) && $(PYTHON) -m http.server 8000

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt
	@echo "Dependencies installed"

# Help command
help:
	@echo "Available commands:"
	@echo "  make build        - Build the site"
	@echo "  make clean        - Remove generated files"
	@echo "  make new-post     - Create a new blog post"
	@echo "  make new-project  - Create a new project"
	@echo "  make serve        - Serve the site locally"
	@echo "  make install      - Install dependencies"
	@echo "  make help         - Show this help message"

# Default target
all: build 