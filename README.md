This is a simple python app that runs an HTTP server exposing the content of an environment variable. This image works fine to run multiple pods with different environment variables and know at which pod are your request arriving (Specially when you are testing routing or service mesh deployments).

Environment variables: MESSAGE = The message the http server will expose when a GET is requested PORT = Is the port the http server will listen to

