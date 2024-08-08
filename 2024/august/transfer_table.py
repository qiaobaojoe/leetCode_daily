def main():

    with open("/Users/majorjoe/Desktop/project-file/transfer_table.sh", "w") as file:

        for i in range(44106, 44130):
            file.write(
                f"curl 'http://finance-car-task.prepub.souche-inc.com/api/vehicle/data/debug/transferTable?vehicleInfoId={i}' -H 'Cookie: _security_token_inc=91719797410377672; _swagger_token=finance_car_task_2022'\n"
            )


if __name__ == "__main__":
    main()
