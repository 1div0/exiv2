// ***************************************************************** -*- C++ -*-
/*
 * Copyright (C) 2021 Exiv2 authors
 * This program is part of the Exiv2 distribution.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, 5th Floor, Boston, MA 02110-1301 USA.
 */

// *****************************************************************************

// included header files
#include "config.h"

#include "isobmff.hpp"
#include "tiffimage.hpp"
#include "image.hpp"
#include "image_int.hpp"
#include "basicio.hpp"
#include "error.hpp"
#include "futils.hpp"
#include "types.hpp"
#include "safe_op.hpp"

// + standard includes
#include <string>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cstdio>

// See section B.1.1 (JPEG 2000 Signature box) of JPEG-2000 specification
const unsigned char JPEG2000Signature[12] = { 0x00, 0x00, 0x00, 0x0c, 0x6a, 0x50, 0x20, 0x20, 0x0d, 0x0a, 0x87, 0x0a };

// *****************************************************************************
// class member definitions
namespace Exiv2
{
    static bool enabled = false;

    EXIV2API void enableISOBMFF()
    {
        enabled = true;
    }

    ISOBMFF::ISOBMFF(BasicIo::UniquePtr io, bool /* create */)
            : Image(ImageType::bmff, mdExif | mdIptc | mdXmp, std::move(io))
    {
    } // ISOBMFF::ISOBMFF

    std::string ISOBMFF::mimeType() const
    {
        switch (fileType)
        {
            case ImageType::avif:
                return "image/avif";

            case ImageType::heif:
                return "image/heif";

            default:
                return "image/unknown";
        }
    }

    void ISOBMFF::setComment(const std::string& /*comment*/)
    {
        // Todo: implement me!
        throw(Error(kerInvalidSettingForImage, "Image comment", "ISO BMFF"));
    } // ISOBMFF::setComment

    static void lf(std::ostream& out, bool& bLF)
    {
        if ( bLF ) {
            out << std::endl;
            out.flush();
            bLF = false ;
        }
    }

    static bool isBigEndian()
    {
        union {
            uint32_t i;
            char c[4];
        } e = { 0x01000000 };

        return e.c[0] != 0;
    }

    static std::string toAscii(long n)
    {
        const auto p = reinterpret_cast<const char*>(&n);
        std::string result;
        bool bBigEndian = isBigEndian();
        for ( int i = 0 ; i < 4 ; i++) {
            result += p[ bBigEndian ? i : (3-i) ];
        }
        return result;
    }

    void ISOBMFF::readMetadata()
    {
    } // ISOBMFF::readMetadata

    void ISOBMFF::printStructure(std::ostream& out, PrintStructureOption option, int depth)
    {
        if (io_->open() != 0)
            throw Error(kerDataSourceOpenFailed, io_->path(), strError());

        // Ensure that this is the correct image type
        if (!isISOBMFFType(*io_, false)) {
            if (io_->error() || io_->eof())
                throw Error(kerFailedToReadImageData);
            throw Error(kerNotAnImage);
        }
    } // ISOBMFF::printStructure

    void ISOBMFF::writeMetadata()
    {
    } // ISOBMFF::writeMetadata

    // *************************************************************************
    // free functions
    Image::UniquePtr newISOBMFFInstance(BasicIo::UniquePtr io, bool create)
    {
        if (!enabled)
        {
            return nullptr;
        }

        Image::UniquePtr image(new ISOBMFF(std::move(io), create));
        if (!image->good())
        {
            image.reset();
        }
        return image;
    }

    bool isISOBMFFType(BasicIo& iIo, bool advance)
    {
        if (!enabled)
        {
            return false;
        }
        const int32_t len = 12;
        byte buf[len];
        iIo.read(buf, len);
        if (iIo.error() || iIo.eof())
        {
            return false;
        }
        bool JPEG2000matched = (memcmp(buf, JPEG2000Signature, len) == 0);
        bool isobmffMatched;
        if (!JPEG2000matched)
        {
            isobmffMatched = buf[4] == 'f' && buf[5] == 't' && buf[6] == 'y' && buf[7] == 'p';
        }
        if (!advance || !JPEG2000matched)
        {
            iIo.seek(-len, BasicIo::cur);
        }
        return JPEG2000matched || isobmffMatched;
    }
}                                       // namespace Exiv2
