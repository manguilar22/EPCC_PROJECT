FROM golang:1.14

# Set necessary environmet variables needed for our image
ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64

# Move to working directory /build
WORKDIR /build

# Copy and download dependency using go mod
COPY go.mod .
COPY go.sum .
RUN go mod download

# Copy the code into the container
COPY . .

# Build the application
RUN go build -o main .

# Move to /dist directory as the place for resulting binary folder
WORKDIR /dist

# Copy binary from build to main folder
RUN cp /build/main .
RUN cp -r /build/data .
RUN cp -r /build/public .

# Export necessary port
EXPOSE 8000

# Command to run when starting the container
CMD ["/dist/main"]