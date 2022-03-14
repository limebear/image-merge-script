import os
import random
from PIL import Image

bg_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/bg')]
body_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/face')]
onhand_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/onhand')]
eyes_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/eyes')]
nose_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/nose')]
mouse_list = [os.path.splitext(filename)[0] for filename in os.listdir('source/mouse')]

for bg in bg_list:
    # import bg
    bg_image = Image.open(f'source/bg/{bg}.png')

    for body in body_list:
        # import body
        face_image = Image.open(f'source/face/{body}.png')
        body_image = Image.open(f'source/body/{body}.png')
        hand_image = Image.open(f'source/frontbody/{body}.png')

        # merge body
        for onhand in onhand_list:

            on_hand_image = Image.open(f'source/onhand/{onhand}.png')

            # merge face artiface
            for eyes in eyes_list:
                eyes_image = Image.open(f'source/eyes/{eyes}.png')


                for nose in nose_list:
                    nose_image = Image.open(f'source/nose/{nose}.png')

                    for mouse in mouse_list:
                        mouse_image = Image.open(f'source/mouse/{mouse}.png')

                        new_image = Image.new('RGB', (1788,1788), (255,255,255))

                        new_image.paste(bg_image, (0,0), bg_image)
                        new_image.paste(body_image, (0,0), body_image)
                        new_image.paste(face_image , (0,0), face_image)
                        new_image.paste(on_hand_image, (0,0), on_hand_image)
                        new_image.paste(hand_image, (0,0), hand_image)

                        new_image.paste(eyes_image, (0,0), eyes_image)
                        new_image.paste(nose_image, (0,0),nose_image)
                        new_image.paste(mouse_image, (0,0), mouse_image)
                    
                        # save image
                        if random.randint(0, 6) == 1:
                            print(f'save {bg}-{body}-{onhand}-{eyes}-{nose}-{mouse}.png')
                            new_image.save(f'result/base/{bg}-{body}-{onhand}-{eyes}-{nose}-{mouse}.png')