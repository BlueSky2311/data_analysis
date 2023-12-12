# set the output file name
set outfile [open RMSF.txt w]
# select the protein atoms from the top molecule and set the first frame as the reference structure
set reference [atomselect 0 "protein" frame 1]
# the frame being compared
set compare [atomselect top "protein"]
# set the number of frames in the trajectory
# change this value according to your trajectory
set num_steps 200

# iterate over all the frames
for {set frame 0} {$frame < $num_steps} {incr frame} {
  # get the correct frame
  $compare frame $frame

  # compute the transformation
  set trans_mat [measure fit $compare $reference]
  # do the alignment
  $compare move $trans_mat
}


# select the alpha-carbon atoms of the protein
set sel [atomselect top "name CA"]
# calculate the RMSF over the entire trajectory
# change the range of frames according to your needs
set rmsf [measure rmsf $sel first 0 last 199 step 1]
# write the RMSF values to the output file
for {set i 0} {$i < [$sel num]} {incr i} {
  puts $outfile "[expr {$i+1}] [lindex $rmsf $i]"
} 
# close the file and delete the selections
close $outfile
$compare delete
$reference delete
$sel delete
