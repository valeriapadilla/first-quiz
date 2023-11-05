package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {
    private int totalMoneyInserted;
    private Map<String, Drink> availableDrinks;

    public static VendingMachine getInstance() {
      return new VendingMachineImpl();
    }

    public VendingMachineImpl() {
        totalMoneyInserted = 0;
        availableDrinks = new HashMap<>();
        availableDrinks.put("ScottCola", new ScottCola());
        availableDrinks.put("KarenTea", new KarenTea());
    }

    @Override
    public void insertQuarter() {
        totalMoneyInserted += 25; 
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (availableDrinks.containsKey(name)) {
            Drink selectedDrink = availableDrinks.get(name);
            int drinkPrice = selectedDrink.getPrice(); 

            if (totalMoneyInserted >= drinkPrice) {
                totalMoneyInserted -= drinkPrice;
                return selectedDrink;
            } else {
                throw new NotEnoughMoneyException();
            }
        } else {
            throw new UnknownDrinkException();
        }
    }

    private static class ScottCola implements Drink {
        @Override
        public String getName() {
            return "ScottCola";
        }

        @Override
        public boolean isFizzy() {
            return true;
        }

        public int getPrice() {
            return 75; 
        }
    }

    private static class KarenTea implements Drink {
        @Override
        public String getName() {
            return "KarenTea";
        }

        @Override
        public boolean isFizzy() {
            return false;
        }

        public int getPrice() {
            return 100; 
        }
    }
}
