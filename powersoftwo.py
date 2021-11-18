function PowersofTwo(num) { 

  var divis;
  var newNum;
  
  divis = num % 2;
  newNum = num / 2;
  while ( divis === 0 && newNum !== 2) {
    divis = newNum % 2;
    newNum = newNum / 2;
  }

  if (newNum === 2) {
    return true;
  }
  else {
    return false;
  }
}