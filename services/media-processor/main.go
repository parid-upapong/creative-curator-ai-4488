package main

import (
	"context"
	"fmt"
	"log"

	"github.com/segmentio/kafka-go"
)

// MediaProcessor handles high-volume asset transformations
func main() {
	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers: []string{"kafka:9092"},
		Topic:   "media_upload",
		GroupID: "media-processor-group",
	})

	fmt.Println("Media Processor Service Started...")

	for {
		m, err := r.ReadMessage(context.Background())
		if err != nil {
			log.Fatal("Error reading message:", err)
		}

		// Process Media Logic
		go processAsset(m.Value)
	}
}

func processAsset(data []byte) {
	// 1. Fetch from S3
	// 2. Run FFmpeg / ImageMagick
	// 3. Update Portfolio Metadata via gRPC
	log.Printf("Processing asset: %s", string(data))
}