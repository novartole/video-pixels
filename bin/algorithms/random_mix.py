import numpy as np
import cv2
import sys

def call(image_full_path, item_width, item_height):
  #print(image, item_width, item_height)
  # count_x = 0
  # count_y = 0

  image = cv2.imread(image_full_path)

  (image_height, image_width) = image.shape[:2]
  # print('shape', image_height, image_width)
  for image_y in range(0, image_height, item_height):
    #print('count_y', count_y)
    #print('image_y', image_y)
    #count_y += 1

    for image_x in range(0, image_width, item_width):
      #print('count_x', count_x)
      #print('image_x', image_x)
      #count_x += 1
      # x , x + image_width - 1
      item = image[image_y:image_y + item_height, image_x:image_x + item_width]
      # print('item_1', item)

      #sequence = item.reshape(item_width * item_height, 1)
      # print('seq_1', sequence)

      #np.random.shuffle(sequence)
      # print('seq_2', sequence)

      #item = sequence.reshape(item_height, item_width, 3)

      # np.random.shuffle(item)
      # print('item shuffled', item)

      # test = item.reshape(6, 3)
      # print('test', test)
      sequence = item.reshape(item_height * item_width, 3)

      np.random.shuffle(sequence)

      # test_2 = item.reshape(3, 2, 3)
      # print('test_2', test_2)
      result = sequence.reshape(item_height, item_width, 3)

      # item_copy = item.copy()
      # np.random.shuffle(item_copy)
      # print('item_copy shuffle', item_copy)

      # random.shuffle(item)
      # print('item_2', item)

      # print('image_before', image[image_y:image_y + item_height, image_x:image_x + item_width])
      image[image_y:image_y + item_height, image_x:image_x + item_width] = result
      # print('image_after', image[image_y:image_y + item_height, image_x:image_x + item_width])
      
  #return image
  cv2.imwrite(image_full_path, image)
      
if __name__ == '__main__':
  # image = np.arange(100).reshape(10, 10)

  # image = np.array(
  # [[[0,0,0], [1,0,0], [2,0,0], [3,0,0]],
  # [[0,1,0], [1,1,0], [2,1,0], [3,1,0]],
  # [[0,2,0], [1,2,0], [2,2,0], [3,2,0]],
  # [[0,3,0], [1,3,0], [2,3,0], [3,3,0]],
  # [[0,4,0], [1,4,0], [2,4,0], [3,4,0]],
  # [[0,5,0], [1,5,0], [2,5,0], [3,5,0]]])
  # print('input', image)

  image = sys.argv[1]
  print(image)

  print(cv2.imread(image))

  result = call(image, 540, 960)
  print('result', result)

  cv2.imwrite(image, result)

  print('image', cv2.imread(image))

  # s = np.arange(5 * 5)
  # print('seq\n', s)

  # random.shuffle(s)
  # print('seq shuffled\n', s)

  # s_reshaped = s.reshape(5, 5,)
  # print('seq reshaped\n', s_reshaped)

  # ss = np.arange(5 * 5).reshape(5, 5).reshape(25, 1)
  # #s_back = s_reshaped.reshape(1, 25)
  # print('seq back\n', ss)