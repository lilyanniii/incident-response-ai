//  prompt user for incident description
// send post request to the endpoint with the message in the JSON body
// print response from api;

package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {

	fmt.Print("What is happening in your system?")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := scanner.Text()
	fmt.Println("User input:", input)

	url := "http://127.0.0.1:8000/analyze"

	payload := map[string]string{"message": input}

	js, _ := json.Marshal(payload)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(js))
	if err != nil {
		fmt.Println("Encountered an error when sending request")
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))

}
