// ======================================================================
// \title  KISSComponent.hpp
// \author Sterling Peet <sterling.peet@ae.gatech.edu>
// \brief  Amateur Radio KISS format packetizer and depacketizer component for use within F Prime.
// ======================================================================

#ifndef KISS_HPP
#define KISS_HPP

#include "HamRadio/KISS/KISSComponentAc.hpp"

namespace HamRadio {

  class KISSComponentImpl :
    public KISSComponentBase
  {

    public:

      // ----------------------------------------------------------------------
      // Construction, initialization, and destruction
      // ----------------------------------------------------------------------

      //! Construct object KISS
      //!
      KISSComponentImpl(
#if FW_OBJECT_NAMES == 1
          const char *const compName /*!< The component name*/
#else
          void
#endif
      );

      //! Initialize object KISS
      //!
      void init(
          const NATIVE_INT_TYPE queueDepth, /*!< The queue depth*/
          const NATIVE_INT_TYPE instance = 0 /*!< The instance number*/
      );

      //! Destroy object KISS
      //!
      ~KISSComponentImpl(void);

    PRIVATE:

      // ----------------------------------------------------------------------
      // Handler implementations for user-defined typed input ports
      // ----------------------------------------------------------------------

      //! Handler implementation for applicationIn
      //!
      void applicationIn_handler(
          const NATIVE_INT_TYPE portNum, /*!< The port number*/
          Fw::Buffer &fwBuffer
      );

      //! Handler implementation for KISSIn
      //!
      void KISSIn_handler(
          const NATIVE_INT_TYPE portNum, /*!< The port number*/
          Fw::Buffer &fwBuffer
      );


    };

} // end namespace HamRadio

#endif
