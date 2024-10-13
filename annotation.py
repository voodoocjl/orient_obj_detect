import cv2
import os
import numpy as np
import argparse

def draw_bounding_boxes(image, category, lines, color=(0, 255, 0)):
    for line in lines:
        data = line.strip().split()
        points = list(map(float, data[1:]))
        points = [int(p) for p in points]
        pts = [(points[i], points[i + 1]) for i in range(1, len(points), 2)]
        pts = np.array(pts, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], isClosed=True, color=color, thickness=2)
        cv2.putText(image, category, (pts[0][0][0], pts[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
    return image

def process_directory(image_dir, txt_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for image_file_name in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_file_name)
        image_name = os.path.splitext(image_file_name)[0]
        if not os.path.isfile(image_path) or not image_path.endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        image = cv2.imread(image_path)
        
        for txt_file in os.listdir(txt_dir):
            txt_path = os.path.join(txt_dir, txt_file)
            if not txt_path.endswith('.txt'):
                continue

            # 提取文件名（不包括扩展名）
            basename = os.path.splitext(txt_file)[0]

            # 提取需要的部分
            category = basename.split('_')[1]

            if not os.path.isfile(txt_path):
                continue
            
            with open(txt_path, 'r') as f:
                lines = [line for line in f.readlines() if line.startswith(image_name)]
                
            if lines:
                color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))  # 随机颜色
                image = draw_bounding_boxes(image, category, lines, color=color)
                
        output_path = os.path.join(output_dir, image_file_name)
        cv2.imwrite(output_path, image)
        print(f'Saved annotated image to {output_path}')

# image_dir = 'data/test_dota_small/test_original'
# txt_dir = 'work_dirs/Task1_results_single'
# output_dir = 'work_dirs/show'

# process_directory(image_dir, txt_dir, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images and annotations")
    parser.add_argument('--image_dir', type=str, required=True, help='Path to the image directory')
    parser.add_argument('--txt_dir', type=str, required=True, help='Path to the annotation directory')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to the output directory')

    args = parser.parse_args()

    process_directory(args.image_dir, args.txt_dir, args.output_dir)
