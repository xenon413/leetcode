SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (
    SELECT OrderS.sales_id FROM OrderS
    WHERE OrderS.com_id IN (
        SELECT Company.com_id FROM Company
        WHERE Company.name = "RED"
    )
);
