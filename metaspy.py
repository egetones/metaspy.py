#!/usr/bin/env python3
import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import sys

def get_decimal_from_dms(dms, ref):
    """
    Converts GPS DMS (Degrees, Minutes, Seconds) to Decimal format.
    """
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    decimal = degrees + minutes + seconds
    
    if ref in ['S', 'W']:
        decimal = -decimal
        
    return decimal

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if not exif_data:
            print("❌ Error: No EXIF data found in this image.")
            return

        print(f"\n🔎 Analyzing: {image_path}")
        print("-" * 40)

        info_dict = {}
        
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            info_dict[tag_name] = value
            
            if tag_name in ['Make', 'Model', 'DateTimeOriginal', 'Software']:
                 print(f"📂 {tag_name}: {value}")

        if 'GPSInfo' in info_dict:
            print("-" * 40)
            print("🌍 GPS Data Found!")
            
            gps_info = info_dict['GPSInfo']
            
            parsed_gps = {}
            for key in gps_info.keys():
                decode = GPSTAGS.get(key, key)
                parsed_gps[decode] = gps_info[key]
            
            if 'GPSLatitude' in parsed_gps and 'GPSLongitude' in parsed_gps:
                lat = get_decimal_from_dms(parsed_gps['GPSLatitude'], parsed_gps['GPSLatitudeRef'])
                lon = get_decimal_from_dms(parsed_gps['GPSLongitude'], parsed_gps['GPSLongitudeRef'])
                
                print(f"📍 Latitude : {lat}")
                print(f"📍 Longitude: {lon}")
                print(f"\n🗺️  Google Maps Link:\nhttps://www.google.com/maps?q={lat},{lon}")
        else:
            print("-" * 40)
            print("⚠️  No GPS data found.")

    except IOError:
        print(f"❌ Error: Unable to open file '{image_path}'.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="MetaSpy - Image Metadata & GPS Extractor")
    parser.add_argument("-i", "--image", required=True, help="Path to the image file")
    
    args = parser.parse_args()
    get_exif_data(args.image)

if __name__ == "__main__":
    main()
