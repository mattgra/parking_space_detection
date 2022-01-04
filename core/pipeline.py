import os
from core.io.mail import send_mail, parse_config
from core.cv.car_detection import run_inference
from core.utils.utils import get_logger, get_timestamp

if __name__ == "__main__":

    # Step 0: Setup
    logger = get_logger()
    logger.log(1, "Step 0: Setting up pipeline ...")
    test_mode = True

    # Step 1: Trigger image
    logger.log(1, "Step 1: Skipping step 1 ...")
    # pass

    # Step 2: Send image from camera device to server / local machine
    logger.log(1, "Step 2: Skipping step 2 ...")
    # pass

    # Step 3: Run inference on input image
    logger.log(1, "Step 3: Running inference")
    inference_result, output_file = run_inference(img_fp="data/test_img_1.png")

    # Step 4: Share result via email
    logger.log(1, "Step 4: Sending email")
    assert len(inference_result), "Inference result is of incorrect type."
    num_cars = len([x for x in inference_result if x == "car"])
    config = parse_config("config/config.yaml")

    if not test_mode:
        send_mail(
            subject=f"Inference result {get_timestamp()}",
            body=f"There are {num_cars} cars.",
            config=config,
        )
