import cv2
from detector import detect
from config import VIDEO_SOURCE, PARKING_SPOTS

cap = cv2.VideoCapture(VIDEO_SOURCE)

print("AI Smart Parking Detection Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    vehicles = detect(frame)
    occupied_count = 0

    for (px1, py1, px2, py2) in PARKING_SPOTS:
        occupied = False

        for (vx1, vy1, vx2, vy2) in vehicles:
            if vx1 < px2 and vx2 > px1 and vy1 < py2 and vy2 > py1:
                occupied = True
                break

        color = (0,0,255) if occupied else (0,255,0)
        label = "Occupied" if occupied else "Free"

        if occupied:
            occupied_count += 1

        cv2.rectangle(frame, (px1, py1), (px2, py2), color, 2)
        cv2.putText(frame, label, (px1, py1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    total_spots = len(PARKING_SPOTS)
    free_spots = total_spots - occupied_count

    cv2.putText(frame, f"Total Spots: {total_spots}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.putText(frame, f"Occupied: {occupied_count}", (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    cv2.putText(frame, f"Free: {free_spots}", (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("AI Smart Parking Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
