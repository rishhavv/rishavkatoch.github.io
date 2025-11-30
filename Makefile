.PHONY: dev build preview clean new-post deploy help

# Directories
BLOG_DIR := src/content/blog
DIST_DIR := dist

# Start development server
dev:
	@echo "Starting dev server at http://localhost:4321"
	@npm run dev

# Build the site
build:
	@echo "Building site..."
	@npm run build
	@echo "Site built successfully in $(DIST_DIR)/"

# Preview production build locally
preview:
	@echo "Previewing production build..."
	@npm run preview

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -rf $(DIST_DIR) .astro node_modules
	@echo "Clean complete"

# Create a new blog post
new-post:
	@read -p "Enter post title: " title; \
	slug=$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-'); \
	date=$$(date +%Y-%m-%d); \
	file="$(BLOG_DIR)/$$slug.md"; \
	echo "---" > "$$file"; \
	echo "title: \"$$title\"" >> "$$file"; \
	echo "date: $$date" >> "$$file"; \
	echo "description: \"Add your description here\"" >> "$$file"; \
	echo "tags: []" >> "$$file"; \
	echo "---" >> "$$file"; \
	echo "" >> "$$file"; \
	echo "Start writing your post here..." >> "$$file"; \
	echo ""; \
	echo "✨ Created new post: $$file"; \
	echo "📝 Edit the file and push to deploy!"

# Deploy (push to GitHub, Actions will handle the rest)
deploy:
	@echo "Deploying to GitHub Pages..."
	@git add .
	@git commit -m "Update site" || echo "Nothing to commit"
	@git push
	@echo "✨ Pushed! GitHub Actions will deploy shortly."

# Install dependencies
install:
	@echo "Installing dependencies..."
	@npm install
	@echo "Dependencies installed"

# Help command
help:
	@echo ""
	@echo "📚 Available commands:"
	@echo ""
	@echo "  make dev        - Start development server (http://localhost:4321)"
	@echo "  make build      - Build the production site"
	@echo "  make preview    - Preview production build locally"
	@echo "  make new-post   - Create a new blog post"
	@echo "  make deploy     - Commit and push to deploy"
	@echo "  make clean      - Remove generated files"
	@echo "  make install    - Install npm dependencies"
	@echo "  make help       - Show this help message"
	@echo ""
	@echo "📁 Blog posts go in: $(BLOG_DIR)/"
	@echo ""

# Default target
all: build
