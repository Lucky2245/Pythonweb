def say_hello():
  message = "Hello, World!" #code will be say_hello()
  print("The file will be saved as index.html")
  f = open("index.html", "w")
  f.write(message)
  f.close()
class noscript():
   message = "<noscript>Please Enable Javascript</noscript>" #code will be noscript
   print("The file will be saved as index.html")
   f = open("index.html", "w")
   f.write(message)
   f.close()
class style():
  message = "<style>p{color:orange;}</style>" #code will be style()
  print("The file will be saved as index.html")
  f = open("index.html", "w")
  f.write(message)
  f.close()
class headerone():
  message = "<h1>Header One</h1>"#code will be headerone()
  print("The file will be saved as index.html")
  f = open("index.html", "w")
  f.write(message)
  f.close()
class script():
  message ="<script></script>"
  print("The file will be saved as index.html")
  f = open("index.html", "w")
  f.write(message)
  f.close()
class run():
  print("running The Code")
  f = open("index.html", "r")
  print(f.read())
class say_goodbye():
  print("Goodbye, World!")
class CookiesEnabled():
  message = "<script>document.write(navigator.cookieEnabled);</script>"
  f = open("index.html", "w")
  f.write(message)
class link(): 
  message ="<a></a>"
