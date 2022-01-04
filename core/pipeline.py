from core.io.mail import send_mail
from core.cv.car_detection import run_inference

if __name__ == '__main__':

    # Step 1: Trigger image
    # pass

    # Step 2: Send image from camera device to server / local machine
    # pass

    # Step 3: Run inference on input image
    inference_result, output_file = run_inference(img_fp='test_img_1.png')

    # Step 4: Share result via email
