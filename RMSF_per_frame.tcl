set reference [atomselect top "protein" frame 1]
set compare [atomselect top "protein"]
set num_steps [molinfo top get numframes]
set output_dir "C:/Users/darkh/Downloads/test/rmsf"

for {set frame 0} {$frame < $num_steps} {incr frame} {
  $compare frame $frame
  set trans_mat [measure fit $compare $reference]
  $compare move $trans_mat
}

for {set k 1} {$k < 200} {incr k} {
  set file_name "RMSF${k}.txt"
  set file_path [file join $output_dir $file_name]
  set outfile [open $file_path w]
  set sel [atomselect top "name CA"]
  set rmsf [measure rmsf $sel first 0 last $k step 1]
  for {set i 0} {$i < [$sel num]} {incr i} {
    puts $outfile "[expr {$i+1}] [lindex $rmsf $i]"
  } 
  close $outfile
}