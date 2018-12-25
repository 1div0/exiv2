#define DEBUG

#include "config.h"

#include "heifimage.hpp"
#include "image_int.hpp"
#include "enforce.hpp"
#include "futils.hpp"
#include "basicio.hpp"
#include "tags.hpp"
#include "tags_int.hpp"
#include "types.hpp"
#include "convert.hpp"

#include <cmath>
#include <iomanip>
#include <string>
#include <cstring>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdio>

const unsigned char HeifSignature[12] = { 0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70, 0x68, 0x65, 0x69, 0x63 };

namespace Exiv2 {
    namespace Internal {

    }}                                      // namespace Internal, Exiv2

namespace Exiv2
{

    HeifImage::HeifImage(BasicIo::UniquePtr io, bool create)
    : Image(ImageType::heif, mdExif | mdXmp, std::move(io))
    {
#ifdef DEBUG
        std::cerr << "Exiv2::HeifImage:: Creating HEIF" << std::endl;
#endif
        (void)create;
    } // HeifImage::HeifImage

    std::string HeifImage::mimeType() const
    {
        return "image/heif";
    }

    Image::UniquePtr newHeifInstance(BasicIo::UniquePtr io, bool create)
    {
        Image::UniquePtr image(new HeifImage(std::move(io), create));
        if (!image->good())
        {
            image.reset();
        }
        return image;
    }

    bool isHeifType(BasicIo& iIo, bool advance)
    {
        const int32_t len = 12;
        byte buf[len];
        iIo.read(buf, len);
        if (iIo.error() || iIo.eof())
        {
            return false;
        }
        bool matched = (memcmp(buf, HeifSignature, len) == 0);
        if (!advance || !matched)
        {
            iIo.seek(-len, BasicIo::cur);
        }
        return matched;
    }

} // namespace Exiv2

