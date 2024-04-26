import java.io.*;
import java.net.*;

public class JavaServer {
    public static void main(String[] args) {
        try {
            // Create a server socket on port 5000
            ServerSocket serverSocket = new ServerSocket(5001);

            while (true) {
                // Wait for a client to connect
                System.out.println("Kuttey");

                Socket clientSocket = serverSocket.accept();

                // Create input and output streams for the client socket
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                // Read a message from the client and print it to the console
                String message = in.readLine();
                System.out.println("Received message from client: " + message);

                // Send a response back to the client
                out.println("Hello from Java server!");

                // Close the client socket
                clientSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
