#!/usr/bin/env python3
"""Generate 6 animated sprite frames from a single sprite image."""

from PIL import Image
import os
import sys

def create_sprite_frames(input_path, output_dir='assets/images'):
    try:
        sprite = Image.open(input_path)
        print(f"✓ Loaded sprite: {input_path}, Size: {sprite.size}")
        
        os.makedirs(output_dir, exist_ok=True)
        
        frame_width = 80
        frame_height = 80
        
        offsets = [(0, 0), (0, -2), (2, -1), (0, 0), (0, 2), (-2, 1)]
        
        for i in range(6):
            frame = Image.new('RGBA', (frame_width, frame_height), (0, 0, 0, 0))
            
            offset_x, offset_y = offsets[i]
            
            sprite_resized = sprite.copy()
            if sprite_resized.width > frame_width - 10 or sprite_resized.height > frame_height - 10:
                max_size = min(frame_width - 10, frame_height - 10)
                sprite_resized.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            
            x = (frame_width - sprite_resized.width) // 2 + offset_x
            y = (frame_height - sprite_resized.height) // 2 + offset_y
            
            if sprite_resized.mode == 'RGBA':
                frame.paste(sprite_resized, (x, y), sprite_resized)
            else:
                frame.paste(sprite_resized, (x, y))
            
            output_path = os.path.join(output_dir, f'character_frame_{i+1}.png')
            frame.save(output_path)
            print(f"✓ Created frame {i+1}: {output_path}")
        
        print(f"\n🎉 Success! Created 6 sprite frames in {output_dir}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 generate_sprite_frames.py <sprite_image_path>")
        sys.exit(1)
    
    input_sprite = sys.argv[1]
    
    if not os.path.exists(input_sprite):
        print(f"❌ Error: File not found: {input_sprite}")
        sys.exit(1)
    
    create_sprite_frames(input_sprite)
