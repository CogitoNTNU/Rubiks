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

# Expose port
EXPOSE 3000

# Run the application
CMD ["npm", "start"]