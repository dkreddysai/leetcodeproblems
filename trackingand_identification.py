import cv2

def main():
    # Initialize video capture
    video_path = ''
    cap = cv2.VideoCapture('highwaycars.mp4')


    # Create a tracker
    tracker = cv2.TrackerMIL_create()  # You can try different trackers like MIL, CSRT, etc.

    # Read the first frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to read video frame")
        return

    # Get user-specified object's initial bounding box
    bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
    tracker.init(frame, bbox)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Update the tracker
        success, new_bbox = tracker.update(frame)

        if success:
            x, y, w, h = map(int, new_bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 20, 0), 2)
            cv2.putText(frame, "Tracked", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 20, 0), 2)
        else:
            cv2.putText(frame, "Lost", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 20), 2)

        cv2.imshow("Object Tracking", frame)

        # Press 'q' to exit
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
