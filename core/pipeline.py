import os
from core.io.mail import send_mail, parse_config
from core.cv.car_detection import run_inference
import time

if __name__ == "__main__":

    # Step 1: Trigger image
    # pass

    # Step 2: Send image from camera device to server / local machine
    # pass

    # Step 3: Run inference on input image
    print(f'[{time.strftime("%Y-%b-%d_%H:%M:%S")}] Step 3: Running inference')
    inference_result, output_file = run_inference(img_fp="data/test_img_1.png")

    # Step 4: Share result via email
    print(f'[{time.strftime("%Y-%b-%d_%H:%M:%S")}] Step 4: Sending email')
    assert len(inference_result), "Inference result is of incorrect type."
    num_cars = len([x for x in inference_result if x == "car"])
    config = parse_config('config/config.yaml')
    send_mail(
        subject=f'Inference result {time.strftime("%Y-%b-%d_%H:%M:%S")}',
        body=f"There are {num_cars} cars.",
        config=config,
    )
