import cv2
import pandas as pd

# Load color CSV
colors = pd.read_csv("colors.csv")

clicked = False
r = g = b = xpos = ypos = 0
color_name = ""

# Function to get closest color name
def get_color_name(R, G, B):
    minimum = float('inf')
    cname = ""
    for i in range(len(colors)):
        d = abs(R - int(colors.loc[i, 'R'])) + abs(G - int(colors.loc[i, 'G'])) + abs(B - int(colors.loc[i, 'B']))
        if d < minimum:
            minimum = d
            cname = colors.loc[i, 'color_name']
    return cname

# Mouse click event
def show_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked, color_name
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = frame[y, x]
        color_name = get_color_name(r, g, b)

# Open webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', show_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        # Draw a filled rectangle to display color
        cv2.rectangle(frame, (20, 20), (750, 60), (int(b), int(g), int(r)), -1)

        # Determine text color for contrast
        text_color = (0, 0, 0) if r + g + b >= 600 else (255, 255, 255)

        text = f"{color_name}  R={r} G={g} B={b}"
        cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2, cv2.LINE_AA)

    cv2.imshow('Color Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
