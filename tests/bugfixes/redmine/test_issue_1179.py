# -*- coding: utf-8 -*-

import system_tests

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

ORIGINAL_FILES = [f"$data_path/exiv2-bug1179{case}.exv"
    for case in char_range('a', 'j')]

def make_command(filename):
    return [f"$exiv2 -pa --grep fuji/i {filename}"]


class CheckFilmMode(metaclass=system_tests.CaseMeta):

    url = "http://dev.exiv2.org/issues/1179"

    commands = [cmd for fname in ORIGINAL_FILES for cmd in make_command(fname)]

    stdout = [
        """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  0 (normal)
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Auto
Exif.Fujifilm.FocusArea                      Short       1  Single Point
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  Off
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.FilmMode                       Short       1  PROVIA (F0/Standard)
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
        """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  0 (normal)
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Auto
Exif.Fujifilm.FocusArea                      Short       1  Single Point
Exif.Fujifilm.FocusPoint                     Short       2  961 939
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  Off
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.FilmMode                       Short       1  Velvia (F2/Fujichrome)
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""", #b
        """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  0 (normal)
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Auto
Exif.Fujifilm.FocusArea                      Short       1  Single Point
Exif.Fujifilm.FocusPoint                     Short       2  961 939
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  Off
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.FilmMode                       Short       1  ASTIA (F1b/Studio Portrait Smooth Skin Tone)
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  0 (normal)
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Auto
Exif.Fujifilm.FocusArea                      Short       1  Single Point
Exif.Fujifilm.FocusPoint                     Short       2  961 939
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  Off
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.FilmMode                       Short       1  CLASSIC CHROME
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  0 (normal)
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Auto
Exif.Fujifilm.FocusArea                      Short       1  Single Point
Exif.Fujifilm.FocusPoint                     Short       2  961 939
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  Off
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.FilmMode                       Short       1  PRO Neg. Hi
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  Monochrome
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Manual
Exif.Fujifilm.FocusArea                      Short       1  Wide
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  On
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  On
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  Monochrome + Ye Filter
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Manual
Exif.Fujifilm.FocusArea                      Short       1  Wide
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Program AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  On
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  On
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  Monochrome + R Filter
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Manual
Exif.Fujifilm.FocusArea                      Short       1  Wide
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Shutter speed priority AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  On
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  Monochrome + G Filter
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Manual
Exif.Fujifilm.FocusArea                      Short       1  Wide
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Shutter speed priority AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  On
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
""",
    """Exif.Fujifilm.Version                        Undefined   4  48 49 51 48
Exif.Fujifilm.SerialNumber                   Ascii      48  FFDT22794526     593332303134151113535030217060
Exif.Fujifilm.Quality                        Ascii       8  NORMAL 
Exif.Fujifilm.Sharpness                      Short       1  0 (normal)
Exif.Fujifilm.WhiteBalance                   Short       1  Auto
Exif.Fujifilm.Color                          Short       1  Sepia
Exif.Fujifilm.WhiteBalanceFineTune           SLong       2  R: 0 B: 0
Exif.Fujifilm.NoiseReduction                 Short       1  n/a
Exif.Fujifilm.HighIsoNoiseReduction          Short       1  0 (normal)
Exif.Fujifilm.FlashMode                      Short       1  Off
Exif.Fujifilm.FlashStrength                  SRational   1  0/100
Exif.Fujifilm.Macro                          Short       1  Off
Exif.Fujifilm.FocusMode                      Short       1  Manual
Exif.Fujifilm.FocusArea                      Short       1  Wide
Exif.Fujifilm.FocusPoint                     Short       2  961 641
Exif.Fujifilm.SlowSync                       Short       1  Off
Exif.Fujifilm.PictureMode                    Short       1  Shutter speed priority AE
Exif.Fujifilm.ExposureCount                  Short       1  1
Exif.Fujifilm.ShadowTone                     SLong       1  0
Exif.Fujifilm.HighlightTone                  SLong       1  0
Exif.Fujifilm.LensModulationOptimizer        Long        1  On
Exif.Fujifilm.ShutterType                    Short       1  Mechanical
Exif.Fujifilm.Continuous                     Short       1  Off
Exif.Fujifilm.SequenceNumber                 Short       1  0
Exif.Fujifilm.BlurWarning                    Short       1  Off
Exif.Fujifilm.FocusWarning                   Short       1  Off
Exif.Fujifilm.ExposureWarning                Short       1  On
Exif.Fujifilm.DynamicRange                   Short       1  Standard
Exif.Fujifilm.DynamicRangeSetting            Short       1  Auto
Exif.Fujifilm.AutoDynamicRange               Short       1  100
Exif.Fujifilm.Rating                         Long        1  0
Exif.Fujifilm.ImageGeneration                Short       1  Original Image
Exif.Fujifilm.FacesDetected                  Short       1  0
Exif.Fujifilm.NumberFaceElements             Short       1  0
"""
    ]
    stderr = [""] * 10
    retval = [0] * 10
