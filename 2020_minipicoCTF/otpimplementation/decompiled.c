#include <stdio.h>

undefined8 main(int param_1,undefined8 *param_2)

{
  byte bVar1;
  int iVar2;
  undefined8 uVar3;
  ulong uVar4;
  long in_FS_OFFSET;
  int local_f0;
  int local_ec;
  char local_e8 [100];
  undefined local_84;
  char local_78 [104];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 < 2) {
    printf("USAGE: %s [KEY]\n",*param_2);
    uVar3 = 1;
  }
  else {
    strncpy(local_e8,(char *)param_2[1],100);
    local_84 = 0;
    local_f0 = 0;
    while( true ) {
      uVar3 = valid_char(local_e8[local_f0]);
      if ((int)uVar3 == 0) break;
      if (local_f0 == 0) {
        uVar4 = jumble(local_e8[0]);
        bVar1 = (byte)((char)uVar4 >> 7) >> 4;
        local_78[0] = ((char)uVar4 + bVar1 & 0xf) - bVar1;
      }
      else {
        uVar4 = jumble(local_e8[local_f0]);
        iVar2 = (int)(char)uVar4 + (int)local_78[local_f0 + -1];
        bVar1 = (byte)(iVar2 >> 0x37);
        local_78[local_f0] = ((char)iVar2 + (bVar1 >> 4) & 0xf) - (bVar1 >> 4);
      }
      local_f0 = local_f0 + 1;
    }
    local_ec = 0;
    while (local_ec < local_f0) {
      local_78[local_ec] = local_78[local_ec] + 'a';
      local_ec = local_ec + 1;
    }
    if (local_f0 == 100) {
      iVar2 = strncmp(local_78,
                      "mlaebfkoibhoijfidblechbggcgldicegjbkcmolhdjihgmmieabohpdhjnciacbjjcnpcfaopigkpdfnoaknjlnlaohboimombk"
                      ,100);
      if (iVar2 == 0) {
        puts("You got the key, congrats! Now xor it with the flag!");
        uVar3 = 0;
        goto LAB_001009ea;
      }
    }
    puts("Invalid key!");
    uVar3 = 1;
  }