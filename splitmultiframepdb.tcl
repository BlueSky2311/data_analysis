##
## A simple VMD script to split multi-frame PDB files into a single PDB 
## structure files and load them up, as in the case of the multi-frame 
## NMR structures provided at the RCSB PDB site.  (example PDB: '1A0N')
##
## Usage:
##   source splitmultiframepdb.tcl
##   mol new 1A0N
##   split_multi_frame_structure top /tmp/myworkarea
##

proc split_multi_frame_structure { whichmol workdir } {
  set allsel [atomselect $whichmol "all"]
  set numframes [molinfo $whichmol get numframes]
  for {set i 0} {$i < $numframes} {incr i} {
    $allsel frame $i
    set filename [format "%s/split%04d.pdb" $workdir $i] 
    file delete $filename
    $allsel writepdb $filename
    mol new $filename
    file delete $filename
  }
  $allsel delete
}


