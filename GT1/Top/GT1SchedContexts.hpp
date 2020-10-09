// ======================================================================
// \title  GT1SchedContexts.hpp
// \author Sterling Peet <sterling.peet@ae.gatech.edu>
// \brief  Demonstration F Prime deployment showing the functionality of the GT-1 mission's payload.
// ======================================================================


#ifndef GT1_TOP_GT1SCHEDCONTEXTS_HPP_
#define GT1_TOP_GT1SCHEDCONTEXTS_HPP_

namespace GT1 {
    // A list of contexts for the rate groups
    enum {
        // CONTEXT_GT1_1Hz = 10, // 1 Hz cycle
        CONTEXT_GT1_10Hz = 11 // 10 Hz cycle
    };
}  // end GT1

#endif /* GT1_TOP_GT1SCHEDCONTEXTS_HPP_ */
