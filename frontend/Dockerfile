# Stage 1: Build the React application
FROM node:21-alpine AS builder

# Set the working directory
WORKDIR /app

# Install dependencies
# Copy only package.json and package-lock.json (if available) first for better caching
COPY package*.json ./

# Install dependencies with npm ci for faster, more reliable builds
RUN npm ci

# Copy the rest of the application source code
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine

# Set environment variables
ENV NODE_ENV=production

# Remove default Nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy the build output from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy custom Nginx configuration (optional but recommended)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]