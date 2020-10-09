// ======================================================================
// \title  KISSComponent.cpp
// \author Sterling Peet <sterling.peet@ae.gatech.edu>
// \brief  Amateur Radio KISS format packetizer and depacketizer component for use within F Prime.
// ======================================================================


#include <HamRadio/KISS/KISSComponent.hpp>
#include "Fw/Types/BasicTypes.hpp"

namespace HamRadio {

  // ----------------------------------------------------------------------
  // Construction, initialization, and destruction
  // ----------------------------------------------------------------------

  KISSComponent ::
#if FW_OBJECT_NAMES == 1
    KISSComponent(
        const char *const compName
    ) :
      KISSComponentBase(compName)
#else
    KISSComponent(void)
#endif
  {

  }

  void KISSComponent ::
    init(
        const NATIVE_INT_TYPE queueDepth,
        const NATIVE_INT_TYPE instance
    )
  {
    KISSComponentBase::init(queueDepth, instance);
  }

  KISSComponent ::
    ~KISSComponent(void)
  {

  }

  // ----------------------------------------------------------------------
  // Handler implementations for user-defined typed input ports
  // ----------------------------------------------------------------------

  void KISSComponent ::
    applicationIn_handler(
        const NATIVE_INT_TYPE portNum,
        Fw::Buffer &fwBuffer
    )
  {
    // TODO
  }

  void KISSComponent ::
    KISSIn_handler(
        const NATIVE_INT_TYPE portNum,
        Fw::Buffer &fwBuffer
    )
  {
    // TODO
  }

} // end namespace HamRadio
