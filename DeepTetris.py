import cv2

from GetScreen import GetScreen
import Processing

def main():

    while True:

        screen = GetScreen('TetrisOnline')
        processed_screen = Processing.ProcessImage(screen)
        cv2.imshow('window', processed_screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


main()