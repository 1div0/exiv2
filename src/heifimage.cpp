// *****************************************************************************
// included header files
#include "config.h"

#include "heifimage.hpp"
#include "tiffimage.hpp"
#include "image.hpp"
#include "image_int.hpp"
#include "basicio.hpp"
#include "error.hpp"
#include "futils.hpp"
#include "types.hpp"
#include "safe_op.hpp"

#include <cmath>
#include <iomanip>
#include <string>
#include <cstring>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdio>

const unsigned char HeifSignature[12] = { 0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70, 0x68, 0x65, 0x69, 0x63 };
const unsigned char HeifBlank[] = { 0x00, 0x00, 0x00, 0x18, 0x66, 0x74, 0x79, 0x70, 0x68, 0x65, 0x69, 0x63 };

// *****************************************************************************
// class member definitions
namespace Exiv2 {
    namespace Internal {

    }}                                      // namespace Internal, Exiv2

namespace Exiv2 {
    using namespace Exiv2::Internal;

    HeifImage::HeifImage(BasicIo::UniquePtr io, bool create)
            : Image(ImageType::heif, mdExif | mdXmp, std::move(io))
    {
        if (create)
        {
            if (io_->open() == 0)
            {
#ifdef DEBUG
                std::cerr << "Exiv2::HeifImage:: Creating HEIF image to memory" << std::endl;
#endif
                IoCloser closer(*io_);
                if (io_->write(HeifBlank, sizeof(HeifBlank)) != sizeof(HeifBlank))
                {
#ifdef DEBUG
                    std::cerr << "Exiv2::HeifImage:: Failed to create HEIF image on memory" << std::endl;
#endif
                }
            }
        }
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

    void HeifImage::readMetadata()
    {
#ifdef DEBUG
        std::cerr << "Exiv2::HeifImage::readMetadata: Reading HEIF file " << io_->path() << std::endl;
#endif
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

    } // HeifImage::readMetadata

    void HeifImage::printStructure(std::ostream& out, PrintStructureOption option, int depth)
    {
        if (io_->open() != 0)
            throw Error(kerDataSourceOpenFailed, io_->path(), strError());

        // Ensure that this is the correct image type
        if (!isHeifType(*io_, false)) {
            if (io_->error() || io_->eof())
                throw Error(kerFailedToReadImageData);
            throw Error(kerNotAHeif);
        }
    }  // HeifImage::printStructure

    void HeifImage::writeMetadata()
    {
        if (io_->open() != 0)
        {
            throw Error(kerDataSourceOpenFailed, io_->path(), strError());
        }
        IoCloser closer(*io_);
        BasicIo::UniquePtr tempIo(new MemIo);
        assert (tempIo.get() != 0);

        doWriteMetadata(*tempIo); // may throw
        io_->close();
        io_->transfer(*tempIo); // may throw

    } // HeifImage::writeMetadata

    void HeifImage::doWriteMetadata(BasicIo& outIo)
    {
        if (!io_->isopen()) throw Error(kerInputDataReadFailed);
        if (!outIo.isopen()) throw Error(kerImageWriteFailed);

#ifdef DEBUG
        std::cout << "Exiv2::HeifImage::doWriteMetadata: Writing HEIF file " << io_->path() << std::endl;
        std::cout << "Exiv2::HeifImage::doWriteMetadata: tmp file created " << outIo.path() << std::endl;
#endif

        // Ensure that this is the correct image type
        if (!isHeifType(*io_, true))
        {
            if (io_->error() || io_->eof()) throw Error(kerInputDataReadFailed);
            throw Error(kerNoImageInInputData);
        }

        // Write HEIF Signature.
        if (outIo.write(HeifSignature, sizeof(HeifSignature)) != sizeof(HeifSignature)) throw Error(kerImageWriteFailed);
#ifdef DEBUG
        std::cout << "Exiv2::HeifImage::doWriteMetadata: EOF" << std::endl;
#endif

    } // HeifImage::doWriteMetadata

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
