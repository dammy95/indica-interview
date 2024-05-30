export default async function Page({ params }: { params: { companyID: string }}) {
    const { companyID } = params;
    const response = await fetch(`http://nginx/api/company/${companyID}/controls/`);
    const errorCode = response.ok ? false : response.status
    const data = await response.json()

    if (errorCode) {
        return <p>Error – could not load company controls page</p>
    }

    console.log({data})

    return (
        <>
            <h2 className="text-black mb-3 text-center">COMPANY CONTROLS PAGE</h2>
            <ul>
                {data.map((control: any) => (
                    <div key={control.id} className="mb-3">
                        <li className="text-black">Control Name: {control.name}</li>
                        <li className="text-black">Control Description: {control.description}</li>
                        <li className="text-black">Control Status: {control.status}</li>
                        <li className="text-black">Last reviewed: {control.last_reviewed}</li>
                    </div>
                ))}
            </ul>
        </>
    )
}
