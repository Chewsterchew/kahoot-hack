from main import kahoot
import threading

def kahoot_run(pin, x, name):
  send = kahoot(pin, name+str(x))
  send.connect()

def test_connection(pin):
  send = kahoot(pin, "Test Name")
  return send.reserve_session()

def start_kahoot_run():
  t = threading.Thread(target=kahoot_run, args=(pin,x,name,))
  t.daemon = True
  t.start()

def get_input():
  pin = input("Enter the Kahoot Game PIN: ")
  name = input("What do you want the base name to be?: ")
  exc = input("How many should join?: ")
  try:
    if (name == None) or (exc == None) or (pin == None):
      print("Error: Input invalid. Please input properly.")
      return None, None, None
    else:
      return int(pin), str(name), int(exc)
  except:
    print("Error: Input invalid. Please input properly")
    error(0,"not proper input", True)

def esc():
  while True:
    esc = input("> ")
    if esc.lower() == 'e':
      break
    else:
      print("> invalid input")

if __name__ == '__main__':
  pin, name, exc = get_input()
  if test_connection(pin):
    print("connecting ...")
    for x in range(exc):
      start_kahoot_run()
    print("\nTask Complete.\nLeave this program running for the accounts to stay.\nType E and press Enter to Exit")
    esc()
  else:
    print("Could not find a game with that pin.")
