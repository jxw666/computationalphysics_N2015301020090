
import time
import os
A=[None]*5
A[0]= '  *       *       *     *   *   *   *    *****   * * *   *****     *  '
A[1]= '  *       *      * *     * *    *   *    *       * * *   *         *  '
A[2]= '  *       *     *****     *     *   *    ****    * * *   ****      *  '
A[3]= '  *       *     *   *    * *    *   *    *       * * *   *         *  '
A[4]= '***       *     *   *   *   *   *****    *****    * *    *****     *  '

B="          "
for j in range(20):
      for t in range(5+j):
         print( A[t])
      time.sleep(1)
      for k in range(5+j):
        A[k]='   '+A[k]
      A.insert(0,B)
      i = os.system('clear')