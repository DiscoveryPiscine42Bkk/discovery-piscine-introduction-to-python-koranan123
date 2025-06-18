while True:
     user_input = input("say something (type 'stop' to exit): ")

     if user_input.upper() == "STOP":
          print("Stopping the program.")
          break

     print(f"I got that: {user_input}")
     