package main

import (
	"bufio"
	"fmt"
	"io"
	"net"
	"os"
)

var port = "localhost:10000"

func main() {
	conn, err := net.Dial("tcp", port)
	if err != nil {
		fmt.Println("ERROR", err)
		os.Exit(1)
	}


	response := bufio.NewReader(conn)


		serverLine, err := response.ReadBytes(byte(1))

		switch err {
		case nil:
			fmt.Print(string(serverLine))
		case io.EOF:
			fmt.Print(string(serverLine))
			os.Exit(0)
		default:
			fmt.Println("ERROR", err)
			os.Exit(2)
		}
		defer conn.Close()
	}
