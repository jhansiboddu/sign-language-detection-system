import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define gesture labels
gesture_labels = {
    0: "FIST",
    1: "GESTURE ONE",
    2: "GESTURE TWO",
    3: "GESTURE THREE",
    4: "GESTURE FOUR",
    5: "GESTURE FIVE"
}

# MediaPipe hand tracking
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm = hand_landmarks.landmark

                # Determine if each finger is up
                fingers = []

                # Thumb (compare tip and base x position based on hand orientation)
                if lm[4].x < lm[3].x:  # Right hand
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other fingers (tip is higher than pip in y-axis)
                for tip in [8, 12, 16, 20]:
                    if lm[tip].y < lm[tip - 2].y:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = sum(fingers)
                label = gesture_labels.get(total_fingers, "UNKNOWN")

                # Display label
                cv2.putText(frame, label, (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

        cv2.imshow("MediaPipe Hand Gestures", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
