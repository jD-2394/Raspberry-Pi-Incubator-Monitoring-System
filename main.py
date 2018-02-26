from sensor import Sensor
import datetime
def main():
    i = None
    print("Enter text (or Enter to quit): ")
    while True:
        r = Sensor()
        r.printReadingF()
        i = raw_input()
        if i == "exit":
            print("program halted")
            break
    

if __name__ == "__main__":
    main()