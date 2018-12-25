#ifndef HEIFIMAGE_HPP
#define HEIFIMAGE_HPP

#include "basicio.hpp"
#include "exif.hpp"
#include "image.hpp"
#include "types.hpp"

#include <string>

#include <libheif/heif.h>

namespace Exiv2
{

    namespace ImageType
    {
        const int heif = 26;
    }

    /*!
      @brief Class to access HEIF files.
     */
    class EXIV2API HeifImage : public Image
    {
    public:
        //! @name Creators
        //@{
        HeifImage(BasicIo::UniquePtr io, bool create);
        //@}

        //! @name Manipulators
        //@{
        void readMetadata();
        void writeMetadata();
        void printStructure(std::ostream& out, PrintStructureOption option,int depth);
        //@}

        /*!
          @brief Not supported. Calling this function will throw an Error(kerInvalidSettingForImage).
         */
        void setComment(const std::string& comment);
        void setIptcData(const IptcData& /*iptcData*/);

        //! @name Accessors
        //@{
        std::string mimeType() const;
        //@}

    private:
        void doWriteMetadata(BasicIo& outIo);
        //! @name NOT Implemented
        //@{
        long getHeaderOffset(byte *data, long data_size,
                             byte *header, long header_size);
        void debugPrintHex(byte *data, long size);
        void decodeChunks(uint64_t filesize);

        //! Copy constructor
        HeifImage(const HeifImage& rhs);
        //! Assignment operator
        HeifImage& operator=(const HeifImage& rhs);
        //@}

    }; //Class HeifImage

    /*!
      @brief Create a new HeifImage instance and return an auto-pointer to it.
             Caller owns the returned object and the auto-pointer ensures that
             it will be deleted.
     */
    EXIV2API Image::UniquePtr newHeifInstance(BasicIo::UniquePtr io, bool create);

    //! Check if the file iIo is a HEIF image.
    EXIV2API bool isHeifType(BasicIo& iIo, bool advance);
}

#endif                                  // HEIFIMAGE_HPP
