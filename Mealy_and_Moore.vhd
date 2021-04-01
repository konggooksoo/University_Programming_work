-- Mealy Machine (mealy.vhd)
-- Asynchronous reset, active low
------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY recog1 IS
PORT(
  x: in STD_ULOGIC;
  clk: in STD_ULOGIC;
  reset: in STD_ULOGIC;
  y: out STD_ULOGIC);
end;

ARCHITECTURE arch_mealy OF recog1 IS
  CONSTANT INIT: STD_ULOGIC_VECTOR (1 DOWNTO 0) :="00";
  CONSTANT FIRST: STD_ULOGIC_VECTOR (1 DOWNTO 0) :="01";
  CONSTANT SECOND: STD_ULOGIC_VECTOR (1 DOWNTO 0) :="10";
  CONSTANT THIRD: STD_ULOGIC_VECTOR (1 DOWNTO 0) :="11";
  SIGNAL curState, nextState: std_ulogic_vector(1 DOWNTO 0);
BEGIN
  combi_nextState: PROCESS(curState, x)
  BEGIN
    CASE curState IS
      WHEN INIT =>
        IF x='0' THEN 
          nextState <= INIT;
        ELSE 
          nextState <= FIRST;
        END IF;
        
      WHEN FIRST =>
        IF x='0' THEN
          nextState <= SECOND;
        ELSE 
          nextState <= FIRST;
        END IF;

      WHEN SECOND =>
        IF x='0' THEN
          nextState <= INIT;
        ELSE 
          nextState <= THIRD;
        END IF;

      WHEN THIRD =>
        IF x='0' THEN
          nextState <= INIT;
        ELSE 
          nextState <= FIRST;
        END IF;
      WHEN OTHERS => nextState <= INIT; ------------Difference------------
    END CASE;
  END PROCESS; -- combi_nextState

  combi_out: PROCESS(curState, x)
  BEGIN
    y <= '0'; -- assign default value
    IF curState = THIRD AND x='0' THEN
      y <= '1';
    END IF;
  END PROCESS; -- combi_output

  seq_state: PROCESS (clk, reset)
  BEGIN
    IF reset = '0' THEN
      curState <= INIT;
    ELSIF clk'EVENT AND clk='1' THEN
      curState <= nextState;
    END IF;
  END PROCESS; -- seq

END; -- arch_mealy


ARCHITECTURE arch_moore OF recog1 IS
  CONSTANT INIT: std_ulogic_vector (2 DOWNTO 0) :="000";
  CONSTANT FIRST: std_ulogic_vector (2 DOWNTO 0) :="001";
  CONSTANT SECOND: std_ulogic_vector (2 DOWNTO 0) :="010";
  CONSTANT THIRD: std_ulogic_vector (2 DOWNTO 0) :="011";
  CONSTANT FOURTH: std_ulogic_vector (2 DOWNTO 0) :="100";
  SIGNAL curState, nextState: std_ulogic_vector(2 DOWNTO 0);
BEGIN
  -----------------------------------------------------
  combi_nextState: PROCESS(curState, x)
  BEGIN
    CASE curState IS
      WHEN INIT =>
        IF x='0' THEN 
          nextState <= INIT;
        ELSE 
          nextState <= FIRST;
        END IF;
        
      WHEN FIRST =>
        IF x='0' THEN
          nextState <= SECOND;
        ELSE 
          nextState <= FIRST;
        END IF;

      WHEN SECOND =>
        IF x='0' THEN
          nextState <= INIT;
        ELSE 
          nextState <= THIRD;
        END IF;

      WHEN THIRD =>
        IF x='0' THEN
          nextState <= FOURTH;
        ELSE 
          nextState <= FIRST;
        END IF;

      WHEN FOURTH =>
        IF x='0' THEN
          nextState <= INIT;
        ELSE 
          nextState <= FIRST;
        END IF;
      WHEN OTHERS => nextState <= INIT; ---------Difference-----------
    END CASE;
  END PROCESS; -- combi_nextState

  combi_out: PROCESS(curState, x)
  BEGIN
    y <= '0'; -- assign default value
    IF curState = THIRD AND x='0' THEN
      y <= '1';
    END IF;
  END PROCESS; -- combi_output

  seq_state: PROCESS (clk, reset)
  BEGIN
    IF reset = '0' THEN
      curState <= INIT;
    ELSIF clk'EVENT AND clk='1' THEN
      curState <= nextState;
    END IF;
  END PROCESS; -- seq

END; -- arch_moore