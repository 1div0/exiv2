// *****************************************************************************
// included header files
#include "config.h"

#include "basicio.hpp"
#include "error.hpp"
#include "enforce.hpp"
#include "futils.hpp"
#include "image.hpp"
#include "image_int.hpp"
#include "heifimage_int.hpp"
#include "types.hpp"

// + standard includes
#include <cassert>
#include <cstring>
#include <iostream>
#include <iterator>
#include <string>

const unsigned char HeifSignature[] = { 0x00, 0x00, 0x00, 0x18, 'f', 't', 'y', 'p', 'h', 'e', 'i', 'c' };

// *****************************************************************************
// class member definitions
namespace Exiv2 {
    using namespace Exiv2::Internal;

    HeifImage::HeifImage(BasicIo::UniquePtr io, bool /*create*/)
            : Image(ImageType::heif, mdExif | mdXmp, std::move(io))
    {
    } // HeifImage::HeifImage

    HeifImage::~HeifImage()
    {
    }

    std::string HeifImage::mimeType() const
    {
        return "image/heif";
    }

    void HeifImage::setComment(const std::string& /*comment*/)
    {
        throw(Error(kerInvalidSettingForImage, "Image comment", "HEIF"));
    } // HeifImage::setComment

    void HeifImage::writeMetadata()
    {
        throw(Error(kerWritingImageFormatUnsupported, "HEIF"));
    } // HeifImage::writeMetadata

    void HeifImage::readMetadata()
    {
        if (io_->open() != 0)
        {
            throw Error(kerDataSourceOpenFailed, io_->path(), strError());
        }
        IoCloser closer(*io_);
        // Ensure that this is the correct image type
        if (!isHeifType(*io_, true))
        {
            if (io_->error() || io_->eof()) throw Error(kerFailedToReadImageData);
            throw Error(kerNotAnImage, "HEIF");
        }

        // pixelWidth_ = heif_image_handle_get_width(handle);
        // pixelHeight_ = heif_image_handle_get_height(handle);

        // int num_metadata;
        // heif_item_id metadata_id;
        // num_metadata = heif_image_handle_get_list_of_metadata_block_IDs(handle, "Exif", &metadata_id, 1);

        // if (num_metadata > 0)
        // {
        //     size_t data_size = heif_image_handle_get_metadata_size(handle, metadata_id);

        //     uint8_t* data = (uint8_t*) alloca(data_size);
        //     err = heif_image_handle_get_metadata(handle, metadata_id, data);
        //     if (err.code)
        //     {
#ifdef EXIV2_DEBUG_MESSAGES
        //         std::cerr << "Exiv2::HeifImage::readMetadata: " << err.message << std::endl;
#endif
        //         throw Error(kerFailedToReadImageData);
        //     }

        //     hexdump (std::cerr, data, data_size);

        //     ByteOrder bo = ExifParser::decode(exifData_, data + 10, data_size - 10);
        //     setByteOrder(bo);
        //     if (data_size > 0 && byteOrder() == invalidByteOrder)
        //     {
#ifndef SUPPRESS_WARNINGS
        //             EXV_WARNING << "Failed to decode Exif metadata.\n";
#endif
        //             exifData_.clear();
        //     }
        //    }
        //     heif_image_handle_release(handle);
        // }

    } // HeifImage::readMetadata

    void HeifImage::printStructure(std::ostream& out, PrintStructureOption option, int depth)
    {
        if (io_->open() != 0)
            throw Error(kerDataSourceOpenFailed, io_->path(), strError());

        // Ensure that this is the correct image type
        if (!isHeifType(*io_, false))
        {
            if (io_->error() || io_->eof())
                throw Error(kerFailedToReadImageData);
            throw Error(kerNotAHeif);
        }
    }  // HeifImage::printStructure

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
        const int32_t len = sizeof(HeifSignature);
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
