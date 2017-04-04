import cv2

def opencv_pixel(image, enc_image):
    img = cv2.imread(image, 0)
    img_enc = cv2.imread(enc_image, 0)
    row, col = img.shape
    rows, cols = img.shape
    total = []
    diff = []
    enc_value = []
    for i in range(row):
        for j in range(col):
            k = img[i, j]
            l = img_enc[i, j]
            total.append(k)
            enc_value.append(l)
            if k != l:
                diff.append(l)
    return total, diff, enc_value

if __name__ == "__main__":
    main()
